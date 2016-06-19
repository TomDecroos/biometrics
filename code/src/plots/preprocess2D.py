'''
Created on 19 Jun 2016

@author: Tom
'''

import matplotlib.pyplot as plt
from classification.preprocess import rotatePoint
from classification.alignment import ScaleRotateTranslate
import math
from plots import saveplot

def preprocess2DImg(face):
    for la in face.face2D.landmarks:
        #print la.name
        if 'Outer left eye corner' in la.name:
            lefteye = la.coor
        if 'Outer right eye corner' in la.name:
            righteye = la.coor
        if 'Nose tip' in la.name:
            nose = la.coor
    
    fig,axs = plt.subplots(1,3)
    fig.set_size_inches(15,5,forward=True)
    img = face.face2D.getImg()
    axs[0].imshow(img)
    x,y = zip(*[lefteye,righteye])
    axs[0].plot(x,y,lw=2,c='green')
    #x,y = zip(*[la.coor for la in face.face2D.landmarks])
    x,y = zip(*[lefteye,righteye,nose])
    axs[0].scatter(x,y,s=50,c='red')
    w,h = img.size
    axs[0].set_xlim(0,w)
    axs[0].set_ylim(h,0)
    
    eye_direction = (righteye[0] - lefteye[0], righteye[1] - lefteye[1])
    # calc rotation angle in radians
    rotation = -math.atan2(float(eye_direction[1]),float(eye_direction[0]))
    img = ScaleRotateTranslate(img, center=nose, angle=rotation)
    #img = CropFace(img, eye_left=left, eye_right=right, offset_pct=(0.01,0.01), dest_sz = (90,100))
    axs[1].imshow(img)
    x,y = zip(*[rotatePoint(nose,la.coor,rotation) for la in face.face2D.landmarks])
    axs[1].scatter(x,y,s=50,c='red')
    
    axs[1].set_xlim(0,w)
    axs[1].set_ylim(h,0)
    
    left = int(min(x))
    top = int(min(y))
    right = int(max(x))
    bottom = int(max(y))
    adjtop = int(top-0.1*(bottom-top))
    
    img = img.crop((left,adjtop,right,bottom))
    axs[2].imshow(img,aspect='equal')
    x = [a-left for a in x]
    y = [a-adjtop for a in y]
    axs[2].scatter(x,y,s=50,c='red')
    w,h = img.size
    axs[2].set_xlim(0,w)
    axs[2].set_ylim(h,0)
    
    fig.tight_layout()
    
if __name__ == '__main__':
    from datalayer.person import loadFaces
    faces = loadFaces('trainset')
    face = faces[16]
    preprocess2DImg(face)
    #saveplot('methods/preprocess2D')
    plt.show()
    for face in faces:
        preprocess2DImg(face)
        plt.show()