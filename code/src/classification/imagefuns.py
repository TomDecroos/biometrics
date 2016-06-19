'''
Created on 18 Jun 2016

@author: Tom
'''
from util.imgtocoors import toCoors
from classification.preprocess import transformed2Dimg
width = 90
height = 100

def get2Dimage(face,index,width = width,height = height,preprocess=False):
    if preprocess:
        img = transformed2Dimg(face)
    else:
        img = face.face2D.getImg()
    img = img.resize((width,height))
    coors = toCoors(img)
    return coors[index]

def get3Dimage(face,width=width,height=height):
    img = face.face3D.getImg().resize((width,height))
    coors = toCoors(img)
    return coors

def getrgbfuns(width=width,height=height,preprocess=False):
    funr = lambda x: get2Dimage(x, 0,width,height,preprocess)
    fung = lambda x: get2Dimage(x, 1,width,height,preprocess)
    funb = lambda x: get2Dimage(x, 2,width,height,preprocess)
    return [funr,fung,funb]

def getcolouranddepthfuns(width=width,height=height):
    imgfuns = getrgbfuns(width,height)
    imgfuns.append(lambda x: get3Dimage(x,width,height))