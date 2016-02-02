'''
Created on Jan 30, 2016

@author: ahanagrawal
'''
from MCM.InfoSpread import runMessage
import numpy as np

def resetFacebookMatrix(N):
    for i in range(len(N)):
        N[i][len(N) + 1] = 0
        N[i][len(N) + 2] = 0


def constructMatrix(fileName):
    
    N = [[0 for x in range(1035)] for x in range(1038)]  
    
    f = open(fileName)
    nodeDict = {}
    line = f.readline()
    
    while(line != ""):
        lineArray = line.split()
        firstIndex = nodeDict.get(lineArray[0])
        secondIndex = nodeDict.get(lineArray[1])
        
        if  firstIndex == None:
            firstIndex = index
            nodeDict[lineArray[0]] = firstIndex 
            
        if  secondIndex == None:
            secondIndex = index
            nodeDict[lineArray[1]] = secondIndex 
        
        first = min(firstIndex, secondIndex)
        second = firstIndex + secondIndex - first
        
        N[firstIndex][secondIndex] = 1
        N[second][first] = 1
        
        
        line = f.readline()

    for j in range(len(N)):
        N[j][len(N)] = np.sum(N[j][0:len(N)])

    return N, index

if __name__ == '__main__':
    
    N,index = constructMatrix("107.edges")
    someList = [0]
    print(runMessage(N, 1, 1, 0, someList))
    print(index)
#     print(len(N))
#     f = open("107.edges")
#     
#     a = f.readline()
#     b = f.readline()
#     print(b)
#     print(a)
    
    