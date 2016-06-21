'''
Created on 19 Jun 2016

@author: Tom
'''
import numpy as np

def product(scores):
    #print np.mean(scores[0]),np.mean(scores[1]),np.mean(scores[2]),np.mean(scores[4])
    return _combiner(scores,lambda a,b:a*b)
def plus(scores):
    return _combiner(scores,lambda a,b:a+b)
def minimum(scores):
    return _combiner(scores,lambda a,b:min(a,b))

def confidence(scores):
    res = []
    for modelscores in scores:
        temp = sorted(modelscores,key=lambda x:x[1])
        conf = (float(temp[1][1] - temp[0][1]) / float(temp[2][1] - temp[0][1]))
        res.append((temp[0][0],conf))
    return res

def _combiner(scores,operator):
    nbmodels = len(scores)
    nbgallery = len(scores[0])
    combinedscores = [t for t in scores[0]]
    for i in range(0,nbgallery):
        for j in range(1,nbmodels):
            old = combinedscores[i]
            add = scores[j][i]
            assert(old[0] == add[0])
            new = (old[0],operator(old[1],add[1]))
            combinedscores[i] = new 
    return combinedscores