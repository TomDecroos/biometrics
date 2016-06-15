'''
Created on 6 Jun 2016

@author: Temp
'''
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

from datalayer.readbntfile import read_bntfile
import matplotlib.pyplot as plt
import numpy as np
from datalayer.landmark import read3DLandmarks
from util.grid import gridCoordinates
from util.imgtocoors import toImg


def read3DFace(facefile):
    data = read_bntfile(facefile + '.bnt')[2]
    x = np.array(data['x'])
    y = np.array(data['y'])
    z = np.array(data['z'])
    landmarks = read3DLandmarks(facefile + '.lm3')
    return Face3D((x,y,z),landmarks)

class Face3D():
    def __init__(self,coors,landmarks):
        self.coors=coors
        self.landmarks=landmarks
    
    def filter(self,coors):
        return zip(*[(xi,yi,zi) for (xi,yi,zi) in zip(*coors)
                     if abs(xi) < 500 and abs(zi) < 500 and abs(yi) < 500])                                                      
        
    def plot(self,nx=100,ny=100,ax = None):
        x,y,z = gridCoordinates(self.filter(self.coors),nx,ny)
        if ax == None:
            fig = plt.figure()
            ax = fig.gca(projection='3d')
        #ax.plot_surface(x,y,z,rstride=2,cstride=2)
        ax.plot_wireframe(x,y,z,rstride=1,cstride=1)
    
    def getImg(self,nx=100,ny=100):
        x,y,z = gridCoordinates(self.filter(self.coors),nx,ny)
        return toImg(z)
    
    def plotDepth(self,nx=100,ny=100,ax=None):
        x,y,z = gridCoordinates(self.filter(self.coors),nx,ny)
        if ax == None:
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
        ax.imshow(z)
        
if __name__ == '__main__':
    face = read3DFace('../../data/bs004/bs004_N_N_0')
    print [x.toString() for x in face.landmarks]
    face.plotDepth()
    plt.show()