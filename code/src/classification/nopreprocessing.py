'''
Created on 18 Jun 2016

@author: Tom
'''
import matplotlib.pyplot as plt
from util.imgtocoors import toCoors
from classification.model import LBPHModel, LBPHFusionModel
from datalayer.person import loadFaces
from datalayer.gallery import getGallery, getProbes
from classification.imagefuns import get3Dimage, getrgbfuns
width=90
height=100
faceset = 'trainset'

faces = loadFaces(faceset)
gallery = getGallery(faces)
probes = getProbes(faces)


def plotGallery():
    imgfuns = getrgbfuns()
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
    
def separatechannels():
    for i in range(0,3):
        model = LBPHModel(getrgbfuns()[i])
        model.train(gallery)
        print 'recognition rate ' + 'rgb'[i]+ ":", model.getRecognitionRate(probes)
    
    model = LBPHModel(get3Dimage)
    model.train(gallery)
    print 'recognition rate 3d:', model.getRecognitionRate(probes)
    
def colour():
    model = LBPHFusionModel(getrgbfuns())
    model.train(gallery)
    print 'recognition rate colour:', model.getRecognitionRate(probes)

def colouranddepth():
    imgfuns = getrgbfuns()
    imgfuns.append(get3Dimage)    
    model = LBPHFusionModel(imgfuns)
    model.train(gallery)
    print 'recognition rate colour and depth:', model.getRecognitionRate(probes)
    
if __name__ == '__main__':
    plotGallery()
    #separatechannels()
    #colour()
    #colouranddepth()