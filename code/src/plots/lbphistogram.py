'''
Created on 20 Jun 2016

@author: tomde_000
'''
from classification.model import LBPHModel
from classification.imagefuns import getrgbfuns
from datalayer.person import loadFaces
from datalayer.gallery import getGallery

faces = loadFaces('trainset')
gallery = getGallery(faces)
face = faces[0]
model = LBPHModel(getrgbfuns(preprocess=False)[0])
model.train(gallery)
print model.recognizers[0].radius()