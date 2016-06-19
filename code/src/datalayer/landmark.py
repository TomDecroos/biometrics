'''
Created on 6 Jun 2016

@author: Temp
'''

def read3DLandmarks(landmarksfile):
    lines = open(landmarksfile,'r').read().split("\n")
    landmarks= []
    for i in range(0,22):
        j = 3+2*i
        name = lines[j]
        coor = tuple([float(c) for c in lines[j+1].split(' ')])
        landmarks.append(Landmark(name,coor))
    return landmarks

def read2DLandmarks(landmarksfile):
    lines = open(landmarksfile,'r').read().split("\n")
    landmarks = []
    for i in range(0,22):
        name = lines[5+i]
        try:
            coor = tuple([float(c) for c in lines[29+i].split(' ')])
        except:
            print landmarksfile
        landmarks.append(Landmark(name,coor))
    return landmarks

class Landmark():
    def __init__(self,name,coor):
        self.name = name
        self.coor = coor
    
    def __str__(self):
        return str((self.name,self.coor))