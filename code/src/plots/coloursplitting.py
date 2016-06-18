'''
Created on 18 Jun 2016

@author: Tom
'''
from datalayer.person import loadFaces
import matplotlib.pyplot as plt
from classification.imagefuns import getrgbfuns
from plots import saveplot
faces = loadFaces('trainset')
face = faces[0]


fig,axs = plt.subplots(1,4)
fig.set_size_inches(10,2.5,forward=True)
axs[0].imshow(face.face2D.getImg().resize((90,100)))
axs[0].set_axis_off()
axs[0].set_title("Colour image",fontsize="medium")
for ax,imgfun,label in zip(axs[1:4],getrgbfuns(90,100),['R-channel','G-channel','B-channel']):
    ax.imshow(imgfun(face))
    ax.set_axis_off()
    ax.set_title(label,fontsize="medium")
saveplot('methods/coloursplitting')
plt.show()