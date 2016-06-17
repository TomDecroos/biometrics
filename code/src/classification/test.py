'''
Created on 15 Jun 2016

@author: Tom
'''

import cv2
from datalayer.person import loadFaces
from util.imgtocoors import toCoors
import numpy as np
import matplotlib.pyplot as plt
#import pprint as pp
# for face in gallery:
#     print face
#trainset = [face for face in faces if face.person < 5]

#pp.pprint(faces)
#gallery = [face.get]

def get_images_and_labels(gallery,imagefun):
    images = []
    labels = []
    for face in gallery:
        img = imagefun(face)
        images.append(img)
        labels.append(face.person)
    return images,labels

def get2Dimage(face):
    img = face.face2D.getImg().resize((100,100))
    coors = toCoors(img)
    return coors[0]
def get3Dimage(face):
    img = face.face3D.getImg()
    coors = toCoors(img)
    return coors

def test(recognizer,probes):
    images,labels = get_images_and_labels(probes,get3Dimage)
    correct = 0
    for img,label in zip(images,labels):
        pred = recognizer.predict(img)
        if label == pred[0]:
            correct += 1
    print "accuracy",float(correct)/float(len(images))
        
def plotgallery(images):
    fig,axs=plt.subplots(1,len(images))
    for ax,img in zip(axs,images):
        print img
        ax.imshow(img)
    plt.show()
    
if __name__ == '__main__':
    faces = loadFaces('trainset')
    gallery = [face for face in faces if face.emotion=="neutral" and face.index ==0]
    images,labels = get_images_and_labels(gallery,get2Dimage)
    plotgallery(images)
    recognizer = cv2.createLBPHFaceRecognizer()
    #print images
    #print labels
    recognizer.train(images,np.array(labels))
    probes = [face for face in faces if face.emotion!="neutral" or face.index !=0]
    test(recognizer,probes)