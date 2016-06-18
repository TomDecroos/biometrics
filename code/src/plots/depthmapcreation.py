'''
Created on 18 Jun 2016

@author: Tom
'''
from datalayer.person import loadFaces
import matplotlib.pyplot as plt
from util.grid import gridCoordinates
from util.imgtocoors import toImg
from classification.imagefuns import get3Dimage
import numpy as np
faces = loadFaces('trainset')
face = faces[0]

fa = face.face3D

fig = plt.figure()
fig.set_size_inches(15,4,forward=True)
ax = fig.add_subplot(1,3,1,projection = '3d')
#ax.set_axis_off()
x,y,z =fa.filter(fa.coors)
ids = np.random.randint(len(x),size=5000)
x=np.array(x)[ids]
y=np.array(y)[ids]
z=np.array(z)[ids]
#x,y,z = gridCoordinates(fa.filter(fa.coors),90,100)
#x = x.flatten();y =y.flatten();z = z.flatten()
ax.scatter(x,y,z,c='blue',s=.5)
ax = fig.add_subplot(1,3,2,projection = '3d')
#ax.set_axis_off()
x,y,z = fa.getCoordinates(50,50)
ax.plot_wireframe(x,y,z)#,cmap='Greys_r')

ax = fig.add_subplot(1,3,3)
ax.imshow(get3Dimage(face))#,cmap='jet')
ax.set_axis_off()
plt.show()