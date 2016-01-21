'''
Created on Dec 26, 2015

@author: ahanagrawal
'''
import numpy as np
import math
from OperationsA.MyFunctions.GoldenSearch import gold

'''
mapMembers is a double array that must be of row length 2.
It stores information on the function's zeros and the function's
search directions.
'''

class MapMembersError(ValueError):
    '''raised when a mapMembers array is passed in that is not of the function's dimension'''
def powell(iterations, mapMembers, startingPoint, function, dimensions, tol = 1 ** -6):
    if (len(mapMembers) != dimensions):
        raise MapMembersError
    
    alreadyInitialized = False
    
    for i in range(2):
        for j in range(0, len(mapMembers[i])):
            if (mapMembers[i][j] != 0):
                alreadyInitialized = True
                break
    
    if (not alreadyInitialized):
        
        lam = 0
        originalP = startingPoint
        for i in range(0, len(mapMembers[0])):
            innerArray = [0 for x in range(dimensions)]
            innerArray[i] = 1 
            mapMembers[0][i] = innerArray
            
    dF = np.zeros(( dimensions + 1))
    
    for j in range(len(mapMembers[0])):
        func = lambda x: function(np.add(originalP,np.multiply(x,mapMembers[0][j])))
        lam = gold(func, lam, True)
        previousF = function(originalP)
        mapMembers[1][j] = np.add(originalP, np.multiply(lam,mapMembers[0][j]))
        newF = function(mapMembers[1][j])
        originalP = mapMembers[1][j]
        dF[j] = math.fabs(np.subtract(previousF, newF))
        
    dir = mapMembers[1][dimensions - 1] - mapMembers[1][0]     
    func = lambda x: function(np.add(originalP,np.multiply(x, dir)))
    lam = gold(func, lam, True)
    previousF = function(originalP)
    lastValue = np.add(originalP, np.multiply(lam,dir))
    newF = function(lastValue)
    dF[j + 1] = math.fabs(np.subtract(previousF, newF))
    
    if (newF - function(mapMembers[1][0]) < tol):
        return lastValue, newF, iterations
    else:
        greatestDecreaseIndex = int(np.argmax(dF))
        for i in range (greatestDecreaseIndex, len(mapMembers[0])):
            mapMembers[0][i] = mapMembers[0][i+1]
            mapMembers[0][dimensions - 1] = dir
            return powell(iterations + 1, mapMembers, startingPoint, function, dimensions, tol)
        
    print(mapMembers)
        
''' A test function that accepts an array of values as its input'''            
def testFunction(a):    
    return (a[0]-5)**2 + (a[1]-5)**2 - 5
    
    
    
    return 0;
    
if __name__ == '__main__':
    a = [[0 for x in range(2)] for x in range(2)]
    print(a)
    dimensions = 2
    startingPoint = [0 for x in range(dimensions)]
    print(powell(1, a, startingPoint, testFunction, dimensions))