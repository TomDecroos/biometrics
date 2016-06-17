'''
Created on 8 Jun 2016

@author: Temp
'''
import numpy as np
import matplotlib.pyplot as plt
from util.imgtocoors import toCoors
import cv2
from datalayer.person import loadFaces
from datalayer.gallery import getGallery, getProbes
from classification.combine import combinePreds

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

class Model(BaseModel):
    
    def __init__(self,recognizer,imgfun):
        self.recognizer = recognizer
        self.imgfun = imgfun
    
    def train(self,gallery):
        images = [self.imgfun(face) for face in gallery]
        labels = np.array([face.person for face in gallery])
        self.recognizer.train(images,labels)
    
    def predict(self, probe):
        return self.recognizer.predict(self.imgfun(probe))
    
    def plot(self,faces):
        _fig,axs=plt.subplots(1,len(faces))
        for ax,face in zip(axs,faces):
            img = self.imgfun(face)
            ax.imshow(img)
        plt.show()

class FusionModel(BaseModel):
    
    def __init__(self,models):
        self.models = models
        
    def train(self, faces):
        for model in self.models:
            model.train(faces)
            
    def predict(self, probe):
        preds = [model.predict(probe) for model in self.models]
        return combinePreds(preds)
        
if __name__ == '__main__':
    def getRimage(face):
        img = face.face2D.getImg().resize((100,100))
        coors = toCoors(img)
        return coors[2]
    
    recognizer = cv2.createLBPHFaceRecognizer()
    model2D = Model(recognizer,getRimage)
    
    faces = loadFaces('trainset')
    model2D.train(getGallery(faces))
    print "recognition rate:", model2D.getRecognitionRate(getProbes(faces))
    model2D.plot(getGallery(faces))
    
    
    
