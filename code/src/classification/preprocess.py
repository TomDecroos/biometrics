'''
Created on 18 Jun 2016

@author: Tom
'''
import math

from PIL import Image

from classification.alignment import CropFace, Distance, ScaleRotateTranslate
from datalayer.person import loadFaces
import matplotlib.pyplot as plt


def transformed2Dimg(face):
    for la in face.face2D.landmarks:
        if 'Outer left eye corner' in la.name:
            lefteye = la.coor
        if 'Outer right eye corner' in la.name:
            righteye = la.coor
        if 'Nose tip' in la.name:
            nose = la.coor
    img = face.face2D.getImg()
    eye_direction = (righteye[0] - lefteye[0], righteye[1] - lefteye[1])
    rotation = -math.atan2(float(eye_direction[1]),float(eye_direction[0]))
    img = ScaleRotateTranslate(img, center=nose, angle=rotation)
    x,y = zip(*[rotatePoint(nose,la.coor,rotation) for la in face.face2D.landmarks])
    left = int(min(x))
    top = int(min(y))
    right = int(max(x))
    bottom = int(max(y))
    img = img.crop((left,top,right,bottom))
    return img
    
    
def rotatePoint(centerPoint,point,angle):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""
    #angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point
    

def cropFace(img,nose):
    pass
if __name__ == '__main__':
    faces = loadFaces('trainset')
    for face in faces:
        if face.person == 2:
            #fig = plt.figure()
            fig,axs = plt.subplots(1,2)
            axs[0].imshow(face.face2D.getImg())
            axs[1].imshow(transformed2Dimg(face))
            plt.show()