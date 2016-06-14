'''
Created on 8 Jun 2016

@author: Temp
'''
import numpy as np
from PIL import Image

def toImg(coors):
    w,h = coors[0].shape
    matrix = np.zeros((w,h,3), dtype = np.int8)
    for i in range(0,3):
        matrix[:,:,i] = coors[i]
    return Image.fromarray(matrix,'RGB')

def toCoors(img):
    matrix =  np.array(img)
    return matrix[:,:,0],matrix[:,:,1],matrix[:,:,2]