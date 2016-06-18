'''
Created on 17 Jun 2016

@author: Tom
'''

def combinePreds(preds):
    labels = {}
    for label,confidence in preds:
        if labels.has_key(label):
            labels[label] += confidence
        else:
            labels[label] = confidence
    #print preds
    return max(labels.items(),key=lambda x:x[1])
    #return max(preds,key=lambda x:x[1])


if __name__ == '__main__':
    x = [(1,0.5),(1,0.78),(2,0.9),(3,0.25)]
    print combinePreds(x)