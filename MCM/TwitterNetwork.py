'''
Created on Feb 1, 2016

@author: ahanagrawal
'''
from MCM.FacebookNetwork import *
from MCM.InfoSpread import *
import networkx as nx
import matplotlib.pyplot as plt


def constructMatrix(fileName, length):
    
    N = [[0 for x in range(length + 3)] for x in range(length)]  
    
    f = open(fileName)
    nodeDict = {}
    index = 0
    line = f.readline()
    
    while(line != "" and index < length):
        lineArray = line.split()
        print(lineArray)
        firstIndex = nodeDict.get(lineArray[0])
        secondIndex = nodeDict.get(lineArray[1])
        
        if  firstIndex == None:
            firstIndex = index
            nodeDict[lineArray[0]] = firstIndex 
            index += 1
            
        if  secondIndex == None:
            secondIndex = index
            nodeDict[lineArray[1]] = secondIndex 
            index += 1
        
        
        
        N[firstIndex][secondIndex] = 1
#         N[second][first] = 1
        N[firstIndex][length + 1] = lineArray[4]
        N[secondIndex][length + 1] = lineArray[4]
        print(lineArray[4])
        #delete this above usually        
        
        line = f.readline()

    for j in range(len(N)):
        N[j][len(N)] = np.sum(N[j][0:len(N)])

    return N, index

def getTimeForTraversal(N, traversalCount, neighborList):
    count = 0
    
    initialTime = int(N[neighborList[0]][len(N) + 1])
    neighborIndex = neighborList[0]
    finalTime = initialTime
    
    while (count < traversalCount and len(neighborList) != 0):
        newList = []
        
        while (len(neighborList) != 0):
            
            neighborIndex = neighborList.pop(0)
            
            
            if (N[neighborIndex][len(N) + 2] == 0 and N[neighborIndex][len(N)] != 0):
                appendNeighbors(newList, neighborIndex, N)
                N[neighborIndex][len(N) + 2] = 1  
        
        count += 1                   
        neighborList = newList
    
#     if (N[neighborIndex][len(N)+1] != 0):        
    finalTime = int(N[neighborIndex][len(N) + 1])
    
    return finalTime - initialTime


if __name__ == '__main__':
    N, index = constructMatrix("retweet.edgelist", 1000)

    f = open("TwitterRuns.txt", 'w')
    for i in range (10):
        for j in range(100):
            neighborList = [int(random.randrange(0,len(N)))]
            time = getTimeForTraversal(N, 1000, neighborList)
            f.write(str(time) + " ")
        f.write("\n")
        
#     A = np.matrix(N)
#     G = nx.to_networkx_graph(A)
#     nx.draw(G)
#     plt.show()
    
    
        
    
