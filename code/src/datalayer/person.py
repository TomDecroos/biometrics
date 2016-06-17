'''
Created on 6 Jun 2016

@author: Temp
'''
import matplotlib.pyplot as plt
from datalayer.face import readFace
import pickle
from datalayer.facetype import getFaceTypes


def readPerson(i,facetypes):
    data = '../../data/'
    folder = "bs00" + str(i) + "/"
    prefix = "bs00" + str(i) + "_"
    postfix = "_0"
    faces = []
    for postfix in ["_0","_1"]:
        for facetype in facetypes.keys():
            middle = facetypes[facetype]
            personfile = data + folder + prefix + middle + postfix
            try:
                face = readFace(personfile)
                faces.append(face)
            except:
                pass
    return Person(i,faces)
    
def readPersons(start=0,end=10):
    facetypes = getFaceTypes()
    return [readPerson(i,facetypes) for i in range(start,end)]

def savePersons(persons):
    f = open('../../data/persons.pkl','w')
    pickle.dump(persons,f)
def saveFaces(faces,name="faces"):
    name += ".pkl"
    f = open('../../data/'+name,'w')
    pickle.dump(faces,f)
    
def loadPersons():
    f = open('../../data/persons.pkl','r')
    return pickle.load(f)
def loadFaces(name="faces"):
    name += ".pkl"
    f = open('../../data/'+name,'r')
    return pickle.load(f)


class Person():
    
    def __init__(self,index,faces):
        self.faces = faces
        self.index = index
    
    def __str__(self):
        value = "person" + str(self.index) + "\n"
        value += "faces: "
        for face in self.faces:
            value += str(face) + " "
        return value

if __name__ == '__main__':
    persons = readPersons(5,10)
    faces = []
    for person in persons:
        for face in person.faces:
            faces.append(face)
            print face
    saveFaces(faces,'testset')
#     savePersons()
#     persons = loadPersons()
#     for person in persons:
#         print person