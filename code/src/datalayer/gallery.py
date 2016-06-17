'''
Created on 17 Jun 2016

@author: Tom
'''

def getGallery(faces):
    return [face for face in faces if face.emotion=="neutral" and face.index ==0]

def getProbes(faces):
    return [face for face in faces if face.emotion!="neutral" or face.index !=0]
    