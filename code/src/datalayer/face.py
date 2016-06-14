'''
Created on 6 Jun 2016

@author: Temp
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from datalayer.face2D import read2DFace
from datalayer.face3D import read3DFace


def readFace(facefile):
    face2D = read2DFace(facefile)
    face3D = read3DFace(facefile)
    return Face(face2D,face3D)

class Face():
    
    def __init__(self,face2D,face3D):
        self.face2D = face2D
        self.face3D = face3D   
    
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(1,2,1)
        self.face2D.plot(ax)
        ax = fig.add_subplot(1,2,2,projection = '3d')
        self.face3D.plot(ax)
        fig.set_size_inches(16,6,forward=True)
        plt.tight_layout()
        
if __name__ == '__main__':
    #face = read3DFace('../../data/bs004/bs004_N_N_0')
    #face.plot()
    face = readFace('../../data/bs004/bs004_N_N_0')
    print [x.toString() for x in face.face2D.landmarks]
    print [x.toString() for x in face.face3D.landmarks]
    face.plot()
    plt.show()