'''
Created on 6 Jun 2016

@author: Temp
'''

import matplotlib.pyplot as plt
from PIL import Image
from datalayer.landmark import read2DLandmarks
from util.grid import resizeMatrix
from util.imgtocoors import toCoors, toImg

def read2DFace(facefile):
    img = facefile + '.png'
    landmarks = read2DLandmarks(facefile + '.lm2')
    return Face2D(img,landmarks)
     
class Face2D():
    def __init__(self,img,landmarks):
        self.img = img
        self.landmarks = landmarks
    
    def getImg(self):
        return Image.open(self.img)
        
    def plot(self,nx=100,ny=100,ax=None):
        if ax==None:
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
        ax.imshow(self.getImg().resize((nx, ny)))
        
        
if __name__ == '__main__':
    #face = read3DFace('../../data/bs004/bs004_N_N_0')
    #face.plot()
    face = read2DFace('../../data/bs004/bs004_N_N_0')
    print [x.toString() for x in face.landmarks]
    face.plot(100,100)
    #plt.show()
    #r,g,b = face.getImg().split()
    #plt.imshow(b)
    #plt.show()
    coors = toCoors(face.getImg())
    print coors
    #print coors.shape
    #img = toImg(coors)
    #plt.imshow(img)
    plt.show()