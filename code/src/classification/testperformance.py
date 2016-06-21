'''
Created on 18 Jun 2016

@author: Tom
'''
from classification.imagefuns import get3Dimage, getrgbfuns
from classification.model import LBPHModel, LBPHFusionModel
from datalayer.gallery import getGallery, getProbes
from datalayer.person import loadFaces
import matplotlib.pyplot as plt
from classification.matchscorecombine import product, plus, minimum, confidence


width=135
height=150
faceset = 'faces'

faces = loadFaces(faceset)
gallery = getGallery(faces)
probes = getProbes(faces)


def plotGallery(preprocess=False):
    imgfuns = getrgbfuns(preprocess=preprocess)
    imgfuns.append(get3Dimage)
    for imgfun,figname in zip(imgfuns,['Rgallerynopre','Ggallerynopre','Bgallerynopre','3Dgallerynopre']):
        fig,axs=plt.subplots(1,len(gallery))
        fig.set_size_inches(10,2,forward=True)
        for j in range(0,len(gallery)):
            img = imgfun(gallery[j])
            ax = axs[j]
            ax.imshow(img)#,cmap='Greys_r')
        fig.tight_layout()
        saveplot(figname)
        plt.show()
    
def saveplot(name,app='.pdf'):
    plt.savefig("../../../report/img/experiments/" + name + app)
    
def separatecolourchannels(preprocess=False):
    for i in range(0,3):
        model = LBPHModel(getrgbfuns(preprocess=preprocess)[i])
        model.train(gallery)
        print 'recognition rate ' + 'rgb'[i]+ ":", model.getRecognitionRate(probes)

def depth():
    model = LBPHModel(lambda x:get3Dimage(x,140,155))
    model.train(gallery)
    print 'recognition rate depth:', model.getRecognitionRate(probes)
    
def colour(preprocess=False,combinefun=product):
    model = LBPHFusionModel(getrgbfuns(preprocess=preprocess),combinefun=combinefun)
    model.train(gallery)
    print 'recognition rate colour:', model.getRecognitionRate(probes)

def colouranddepth(preprocess=False,combinefun=product):
    imgfuns = getrgbfuns(preprocess=preprocess)
    imgfuns.append(lambda x:get3Dimage(x,width,height))
    model = LBPHFusionModel(imgfuns,combinefun=combinefun)
    model.train(gallery)
    print 'recognition rate colour and depth:', model.getRecognitionRate(probes)
    
if __name__ == '__main__':
    #plotGallery(True)
    separatecolourchannels(True)
    #depth()
    colour(True,combinefun=product)
    colouranddepth(preprocess=True,combinefun=product)
