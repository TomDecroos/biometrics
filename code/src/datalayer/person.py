'''
Created on 6 Jun 2016

@author: Temp
'''
import matplotlib.pyplot as plt
from datalayer.face import readFace
import pickle

def getFaceTypes():
    return {'anger' : 'E_ANGER',
             'disgust' : 'E_DISGUST',
             'fear' : 'E_FEAR',
             'happy' : 'E_HAPPY',
             'sadness' : 'E_SADNESS',
             'surprise' : 'E_SURPRISE',
             'neutral' : 'N_N',
             'obscured' : 'O_EYE'
             }

def readPerson(i,facetypes):
    data = '../../data/'
    folder = "bs00" + str(i) + "/"
    prefix = "bs00" + str(i) + "_"
    postfix = "_0"
    faces = {}
    for postfix in ["_0","_1"]:
        for facetype in facetypes.keys():
            middle = facetypes[facetype]
            personfile = data + folder + prefix + middle + postfix
            try:
                face = readFace(personfile)
                emotion = facetype if postfix == "_0" else facetype + postfix
                faces[emotion] = face
            except:
                pass
    return Person(faces)
    
def readPersons():
    facetypes = getFaceTypes()
    facetypes.pop('obscured')
    return [readPerson(i,facetypes) for i in range(0,10)]


def savePersons():
    facetypes = getFaceTypes()
    facetypes.pop('obscured')
    persons = readPersons()
    f = open('../../data/persons.pkl','w')
    pickle.dump(persons,f)

def loadPersons():
    f = open('../../data/persons.pkl','r')
    return pickle.load(f)

class Person():
    
    def __init__(self,faces):
        self.faces = faces

if __name__ == '__main__':
    persons = loadPersons()
    person = persons[3]
    for face in person.faces.values():
        face.plot()
        plt.show()