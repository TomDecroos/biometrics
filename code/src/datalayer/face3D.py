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
from util.imgtocoors import toImg, toCoors


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
        x,y,z = self.getCoordinates(nx, ny)
        if ax == None:
            fig = plt.figure()
            ax = fig.gca(projection='3d')
        #ax.plot_surface(x,y,z,rstride=2,cstride=2)
        ax.plot_wireframe(x,y,z,rstride=1,cstride=1)
#         
#         def transformla(la):
#             return la[0],la[1],la[2]+150
#         x,y,z=zip(*[transformla(la.coor) for la in self.landmarks])
#         ax.scatter(x,y,z,c='red')
    
    def getCoordinates(self,nx=100,ny=100):
        x,y,z = gridCoordinates(self.filter(self.coors),nx,ny)
        _min =  np.min(z[np.where(np.invert(np.isnan(z)))])
        _max = np.max(z[np.where(np.invert(np.isnan(z)))])
        z[np.where(np.isnan(z))] = _min
        z -= _min
        #z = 200*(z-_min)
        #z = z/(_max-_min)
        n,m =z.shape
        z1 = np.zeros((n,m))
        for i in range(0,n):
            for j in range(0,m):
                z1[i,j] = z[n-1-i,j]
        return x,y,z1
    
    def getImg(self,nx=100,ny=100):
        coors = self.getCoordinates(nx, ny)
        return toImg(coors[2])
    
    def plotDepth(self,nx=100,ny=100,ax=None):
        z = self.getImg(nx,ny)
        if ax == None:
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
        ax.imshow(z)
        
    def plotDepthandLandmarks(self,nx=90,ny=100):
        x,y,z = gridCoordinates(self.filter(self.coors),nx,ny)
        top = min(y.flatten())
        bottom = max(y.flatten())
        left = min(x.flatten())
        right = max(x.flatten())
        
        def transformLA(landmark):
            x = int(nx*(landmark.coor[0]-left)/(right-left))
            y = int(nx*(landmark.coor[1]-top)/(bottom-top))
            return x,ny-y
        
        plt.imshow(self.getImg())
        x,y = zip(*[transformLA(landmark) for landmark in self.landmarks])
        plt.scatter(x,y)
        plt.show()
            
if __name__ == '__main__':
    face = read3DFace('../../data/bs004/bs004_N_N_0')
    print [x for x in face.landmarks]
    face.plot()
    #face.plotDepth(200,200)
    plt.show()
    #face.plotDepthandLandmarks(90, 100)