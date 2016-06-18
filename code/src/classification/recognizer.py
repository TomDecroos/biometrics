'''
Created on 17 Jun 2016

@author: Tom
'''

class BaseModel:
    
    def train(self,faces):
        raise NotImplementedError
    def predict(self,face):
        raise NotImplementedError

class Model(BaseModel):
    
    def __init__(self,recognizer,imgfun):
        