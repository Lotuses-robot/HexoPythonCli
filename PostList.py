from array import array
import utils
import os
utils.chdir(2)
lsdir = os.listdir('.')
List = [i.replace('-', ' ') for i in lsdir if os.path.isdir(os.path.join('.', i))]
for i in range(0, len(List)):
    print(i,'<' + List[i] + '>')

def getRetList():
    utils.chdir(2)
    lsdir = os.listdir('.')
    List = ['<' + i.replace('-', ' ') + '>' for i in lsdir if os.path.isdir(os.path.join('.', i))]
    return List