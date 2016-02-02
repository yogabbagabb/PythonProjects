'''
Created on Jan 30, 2016

@author: ahanagrawal
'''

import numpy as np
import random
import matplotlib.pyplot as plt

import networkx as nx

'''
[i][vertexNumber] = neighbors
[i][vertexNumber + 1] = hits
[i][vertexNumber + 2] = informed or uninformed (1 or 0)
'''
def createGraph(vertexNumber, timePeriod):
    N = [[0 for x in range(vertexNumber + 3)] for x in range(vertexNumber)]
    for i in range(vertexNumber):
        for j in range(vertexNumber):
            N[i][j] = 1 if (random.random() < timePeriod) else 0
        N[i][vertexNumber] = (np.sum(N[i][0:vertexNumber]) - N[i][i])
    
    return N

'''
neighborList is a list of adjacency matrix entries. It initially contains one node.
'''
def runMessage(N, sensitivity, channels, startingNode, neighborList):
    
#     if N[currentNode][len(N) + 2] == 0:
    trials = 0
    
    while (len(neighborList) != 0):
        trials += 1
        newList = []
        
        while (len(neighborList) != 0):
            
            neighborIndex = neighborList.pop()
            
            
            if (N[neighborIndex][len(N) + 2] == 0 
                and N[neighborIndex][len(N)] != 0):
            
                probability = (sensitivity + channels 
                + getHitProportion(N, neighborIndex))/3
                
                if (random.random() <= probability):
                    appendNeighbors(newList, neighborIndex, N)
                    N[neighborIndex][len(N) + 2] = 1
                    
                else:
                    newList.append(neighborIndex)
                    
        neighborList = newList
                    
                
    return trials
            
    
def appendNeighbors(someList, index, N):
    for i in range(len(N)):
        if (N[index][i] == 1):
            someList.append(i)
        

def getHitProportion(N, vertex):    
    hits = 0
    for i in range(len(N)):
        if (N[vertex][i] == 1 and N[i][len(N) + 2] == 1):
            hits += 1
        N[vertex][len(N) + 1] = hits
        
    neighbors = N[vertex][len(N)]
    
    
    return (hits/neighbors)

        
            
            
    
    
    


if __name__ == '__main__':
    array = createGraph(1035,0.25)
    someList = [0]
    
    print(runMessage(array, 0.25, 0.25, 0, someList))
#     a = np.asarray(array)
#     print(a)
#     a,b = np.hsplit(a, [len(a)])
#     g = nx.DiGraph(a)
#     g = nx.to_networkx_graph(a)
#     print(nx.average_clustering(g))
#     print(a)
    