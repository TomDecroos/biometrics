'''
Created on 19 Jun 2016

@author: Tom
'''
def product(scores):
    nbmodels = len(scores)
    nbgallery = len(scores[0])
    combinedscores = [t for t in scores[0]]
    for i in range(0,nbgallery):
        for j in range(1,nbmodels):
            old = combinedscores[i]
            add = scores[j][i]
            assert(old[0] == add[0])
            new = (old[0],old[1]*add[1])
            #print old,new
            combinedscores[i] = new 
    #print "scores", scores
    #print "combinedscores", combinedscores
    return combinedscores