'''
Created on 6 Jun 2016

@author: Temp
'''

import matplotlib.pyplot as plt
from PIL import Image
from datalayer.landmark import read2DLandmarks
import math
from classification.alignment import ScaleRotateTranslate
from classification.preprocess import rotatePoint

def read2DFace(facefile):
    img = facefile + '.png'
    landmarks = read2DLandmarks(facefile + '.lm2')
    return Face2D(img,landmarks)
     
class Face2D():
    def __init__(self,img,landmarks):
        self.img = img
        self.landmarks = landmarks
        self._img = None
        self._transformedimg = None
        
    def getImg(self):
        if not self._img:
            self._img = Image.open(self.img)
        return self._img
    
    def getTransformedImg(self):
        if not self._transformedimg:
            for la in self.landmarks:
                if 'Outer left eye corner' in la.name:
                    lefteye = la.coor
                if 'Outer right eye corner' in la.name:
                    righteye = la.coor
                if 'Nose tip' in la.name:
                    nose = la.coor
            img = self.getImg()
            eye_direction = (righteye[0] - lefteye[0], righteye[1] - lefteye[1])
            rotation = -math.atan2(float(eye_direction[1]),float(eye_direction[0]))
            img = ScaleRotateTranslate(img, center=nose, angle=rotation)
            x,y = zip(*[rotatePoint(nose,la.coor,rotation) for la in self.landmarks])
            left = int(min(x))
            top = int(min(y))
            right = int(max(x))
            bottom = int(max(y))
            #adjtop = int(top-0.1*(bottom-top))
            self._transformedimg = img.crop((left,top,right,bottom))
        return self._transformedimg
        
        
    def plot(self,nx=100,ny=100,ax=None):
        if ax==None:
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
        ax.imshow(self.getImg().resize((nx, ny)))
        
        
if __name__ == '__main__':
    #face = read3DFace('../../data/bs004/bs004_N_N_0')
    #face.plot()
    face = read2DFace('../../data/bs004/bs004_N_N_0')
    print [x for x in face.landmarks]
    face.plot(100,100)
    plt.show()
    img = face.getTransformedImg()
    plt.imshow(img)
    plt.show()
    img = face.getTransformedImg()
    plt.imshow(img)
    plt.show()
    #r,g,b = face.getImg().split()
    #plt.imshow(b)
    #plt.show()
#     coors = toCoors(face.getImg())
#     print coors
#     #print coors.shape
#     #img = toImg(coors)
#     #plt.imshow(img)
#     plt.show()