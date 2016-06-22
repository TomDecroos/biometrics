'''
Created on 8 Jun 2016

@author: Temp
'''
import numpy as np
import matplotlib.pyplot as plt
from util.imgtocoors import toCoors
import cv2
from datalayer.gallery import getGallery, getProbes
from classification.combine import combinePreds
from classification.imagefuns import get2Dimage, get3Dimage
from classification.matchscorecombine import product

class BaseModel:
    
    def train(self,gallery):
        raise NotImplementedError
    def predict(self,probe):
        raise NotImplementedError
    
    def getRecognitionRate(self,probes):
        correct = 0
        labels = [face.person for face in probes]
        preds = [self.predict(face) for face in probes]
        for pred,label in zip(preds,labels):
            if label == pred[0]:
                correct += 1
        return float(correct)/float(len(probes))

class SimpleModel(BaseModel):
    
    def __init__(self,recognizer,imgfun):
        self.recognizer = recognizer
        self.imgfun = imgfun
    
    def plot(self,faces):
        _fig,axs=plt.subplots(1,len(faces))
        for ax,face in zip(axs,faces):
            img = self.imgfun(face)
            ax.imshow(img)
        plt.show()
        
    def train(self,gallery):
        images = [self.imgfun(face) for face in gallery]
        labels = np.array([face.person for face in gallery])
        self.recognizer.train(images,labels)
    
    def predict(self, probe):
        return self.recognizer.predict(self.imgfun(probe))  

class EigenModel(SimpleModel):
    
    def __init__(self, imgfun):
        SimpleModel.__init__(self,cv2.createEigenFaceRecognizer(), imgfun)
    
  
class BaseFusionModel(BaseModel):
    
    def __init__(self,models):
        self.models = models
        
    def train(self, faces):
        for model in self.models:
            model.train(faces)
        
    def plot(self,faces):
        _fig,axs=plt.subplots(len(self.models),len(faces))
        for i in range(0,len(self.models)):
            for j in range(0,len(faces)):
                img = self.models[i].imgfun(faces[j])
                ax = axs[i][j] if len(self.models) > 1 else axs[j]
                ax.imshow(img)#,cmap='Greys_r')
        #fig.tight_layout()
        plt.show()
        
class SimpleFusionModel(BaseFusionModel):
    
    def predict(self, probe):
        preds = [model.predict(probe) for model in self.models]
        labels = {}
        for label,confidence in preds:
            if labels.has_key(label):
                labels[label] += confidence
            else:
                labels[label] = confidence
        return min(labels.items(),key=lambda x:x[1])

class MatchScoreModel(BaseModel):
    
    def predict(self,probe):
        scores = self.getMatchScores(probe)
        best = min(scores,key=lambda x:x[1])
        return best

class LBPHModel(MatchScoreModel):
    
    def __init__(self,imgfun):
        self.imgfun = imgfun
        self.recognizers = []
        
    def train(self,gallery):
        for face in gallery:
            img = [self.imgfun(face)]
            label = np.array([face.person])
            recognizer = cv2.createLBPHFaceRecognizer()
            recognizer.train(img,label)
            self.recognizers.append(recognizer)
    
    def plot(self,faces):
        _fig,axs=plt.subplots(1,len(faces))
        for ax,face in zip(axs,faces):
            img = self.imgfun(face)
            ax.imshow(img)
        plt.show()
    
    def getMatchScores(self,probe):
        img = self.imgfun(probe)
        return [recognizer.predict(img) for recognizer in self.recognizers]

class MatchScoreFusionModel(BaseFusionModel,MatchScoreModel):
    
    def __init__(self, models,combinefun=product):
        BaseFusionModel.__init__(self, models)
        self.combinefun = combinefun
        
    def getMatchScores(self,probe):
        scores = [model.getMatchScores(probe) for model in self.models]
        return self.combinefun(scores)
    def predict(self,probe):
        return MatchScoreModel.predict(self, probe)

class LBPHFusionModel(MatchScoreFusionModel):
    def __init__(self, imgfuns,combinefun=product):
        models = [LBPHModel(imgfun) for imgfun in imgfuns]
        MatchScoreFusionModel.__init__(self, models,combinefun)
    
if __name__ == '__main__':
    from datalayer.person import loadFaces
    def get2DModel(index):
        recognizer = cv2.createLBPHFaceRecognizer()
        return SimpleModel(recognizer,lambda x: get2Dimage(x,index))
    
#     models= []
#     models = [get2DModel(i) for i in range(0,3)]
#     #models.append(Model(cv2.createLBPHFaceRecognizer(),get3Dimage))
#     model = SimpleFusionModel(models)
    #model =  SimpleModel(cv2.createLBPHFaceRecognizer(),lambda x: get2Dimage(x,0))
    #imgfuns = [(lambda x: get2Dimage(x, index)) for index in range(0,2)]
    fun1 = lambda x: get2Dimage(x,0)
    fun2 = lambda x : get2Dimage(x, 1)
    fun3 = lambda x : get2Dimage(x, 2)
    fun4 = lambda x: get3Dimage(x)
    imgfuns = [fun1,fun2,fun3,fun4]
    model2 = LBPHFusionModel(imgfuns)
    faces = loadFaces('faces')
#     model.train(getGallery(faces))
    model2.train(getGallery(faces))
# #     rr = model.getRecognitionRate(getProbes(faces))
# #     print "simple recognition rate:", rr
    rr = model2.getRecognitionRate(getProbes(faces))
    print "recognition rate:", rr
    model2.plot(getGallery(faces))
    
    
    
