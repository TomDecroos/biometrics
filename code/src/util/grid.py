'''
Created on 8 Jun 2016

@author: Temp
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def gridCoordinates((x,y,z),nx,ny):
    x1 = np.linspace(min(x),max(x),nx)
    y1 = np.linspace(min(y),max(y),ny)
    x1,y1 = np.meshgrid(x1,y1)
    print "before griddata"
    z1 = griddata((x,y),z,(x1,y1))
    print "after griddata"
    return x1,y1,z1

def resizeMatrix(z,nx,ny):
    print "resize"
    n,m = z.shape
    x,y = np.meshgrid(range(0,n),range(0,m))
    z1 = gridCoordinates((list(x.flat),list(y.flat),list(z.flat)),nx,ny)[2]
    return np.reshape(z1, (nx,ny))

if __name__ == '__main__':
    
    x = np.random.rand(9,9)
    fig = plt.figure()
    ax = fig.add_subplot(1,2,1)
    ax.imshow(x)
    ax = fig.add_subplot(1,2,2)
    y = resizeMatrix(x, 8, 8)
    ax.imshow(y)
    plt.show()
    