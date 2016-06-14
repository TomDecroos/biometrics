'''
Created on 6 Jun 2016

@author: Temp
'''

def getFaceTypes():
    return {'anger' : 'E_ANGER',
             'disgust' : 'E_DISGUST',
             'fear' : 'E_FEAR',
             'happy' : 'E_HAPPY',
             'sadness' : 'E_SADNESS',
             'surprise' : 'E_SURPRISE',
             'neutral' : 'N_N',
             'obscured' : 'O_EYES'
             }
             

if __name__ == '__main__':
    print getFaceTypes()