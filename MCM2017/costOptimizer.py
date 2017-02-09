'''
Created on Jan 22, 2017

@author: ahanagrawal
'''


import numpy as np

import decimal

def drange(x, y, jump):
    while x < y:
        yield float(x)
        x += float(decimal.Decimal(jump))

def powerset(s):
    listOfLists = list()
    x = len(s)
    for i in range(1 << x):
        innerList = list()
        for j in range (x):
            if (i & (1 << j)):
                innerList.append(s[j])
        listOfLists.append(innerList)
    return listOfLists

def constructTuple(power, length):
    finishedTuples = list()
    for aList in power:
        ones = np.ones((1,length), int)
        finTuple = list()
        for num in aList:
            ones[0,num-1] += 1
            ones[0, num] -= 1
        
        total = 0
        
        i = 0
        while i < (length):
            
            if (i == length-1):
                finTuple.append(1)
                i += 1
            elif ones[0,i] <= ones[0, i+1]:
                finTuple.append(1)
                i += 1
            else:
                j = i+1
                total = ones[0,i]
                while (ones[0,j] != 0):
                    total += ones[0,j]
                    j += 1
                finTuple.append(total)
                i = j+1
                
                total = 0
#         if total != 0:
#             for j in range(total):
#                 finTuple.append(1)
        finishedTuples.append(finTuple)
            
    
    return finishedTuples

def delta(a, b, Delta):
    return sum(Delta[a:a+b])

def minimize(finishedLists, delta, Delta, M, L, length, X = 8000, Y = 2200):
    #assuming 40 ft, 275 * 8 = 2200
    #8000 for 1 portable traffic light
    costDict = dict()
    theMin = 0 # garbage right now
    firstTime = True
    
    for eachList in finishedLists:
        
        validEntry = True
        numberGreaterThanThree = 0
        totalGone = 0
        for entry in eachList:
            theLambda = delta(totalGone, entry, Delta)
            if (entry >= 3):
                numberGreaterThanThree += 1
            totalGone += entry
            if (theLambda/M > 1 or len(eachList) != L):
                validEntry = False
                break
        
        if (validEntry and len(eachList) == L):    
            trafficLights = numberGreaterThanThree
            walls = length - 1
            costDict[trafficLights*X + walls*Y] = eachList
            
            if firstTime:
                theMin = trafficLights*X + walls*Y
                firstTime = False
    
    for key in costDict:
        if key < theMin:
            theMin = key
    
    return costDict[theMin]


def distribution():            
    thePower = powerset([1,2,3,4,5,6,7])
    for x in thePower:
        print (x)
    print("\n")
    theTuples = constructTuple(thePower, 8)
    for x in theTuples:
        print (x)
        
    Delta = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
    DeltaTwo = [0.05, 0.05, 0.06, 0.06, 0.05, 0.04, 0.04, 0.04]
    DeltaThree = [0.04, 0.06, 0.06, 0.06, 0.06, 0.04, 0.04, 0.04]

    print(Delta, minimize(theTuples, delta, Delta, 0.20, 3, 8))
    print(DeltaTwo, minimize(theTuples, delta, DeltaTwo, 0.20, 3, 8))
    print(DeltaThree, minimize(theTuples, delta, DeltaThree, 0.20, 3, 8))
    
#     print("\n")
# 
#     for i in drange(0, 0.10, '0.0025'):
#         Doddy = np.array(Delta)
#         Doddy[0:8] += i
#         print(Doddy, minimize(theTuples, delta, Doddy, 0.20, 3, 8))
    
def trafficIncrease():            
    thePower = powerset([1,2,3,4,5,6,7])
    for x in thePower:
        print (x)
    print("\n")
    theTuples = constructTuple(thePower, 8)
    for x in theTuples:
        print (x)
        
    Delta = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]

    
    print("\n")

    for i in drange(0, 0.10, '0.0025'):
        Doddy = np.array(Delta)
        Doddy[0:8] += i
        print(Doddy, minimize(theTuples, delta, Doddy, 0.20, 3, 8))
        
def autonomous():            
    thePower = powerset([1,2,3,4,5,6,7])
    for x in thePower:
        print (x)
    print("\n")
    theTuples = constructTuple(thePower, 8)
    for x in theTuples:
        print (x)
        
    Delta = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]

    
    print("\n")

    for i in drange(0, 0.10, '0.0025'):
        Doddy = np.array(Delta)
        Doddy[0:2] += i
        Doddy[0:8] -= 0.2*i
        print(Doddy, minimize(theTuples, delta, Doddy, 0.20, 3, 8))
    
    
if __name__ == '__main__':
    distribution()