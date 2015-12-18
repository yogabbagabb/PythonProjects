'''
Created on Dec 2, 2015

@author: ahanagrawal


Performs gaussian elimination with pivoting.

Determines which row is "dominant" and swaps that row with the current one in the process of performing
Gaussisan elimination.

The most dominant row is defined as the row having the relatively greatest
leading term. A row with "relatively greatest leading term" has the greatest ration of row[currentIndex, currentIndex]/Max(A[currentIndex,:])

'''

import numpy as np


'''
Precondition: a, The array to perform gaussian elimination on, is n  x n; b, the solution array is of length n
Postcondition: a and will be modified. Returns x, the modified array and y, the solution vector. 
'''
def gausspivot(a,b):
    a = a.astype(float)
    for i in range (0, len(a)-1):
        toSwap = getGreatestRelativeRow(a,i)
        swapRows(a,i, toSwap)
        swapRows(b,i, toSwap)
        for j in range(i+1, len(a)):
            lam = a[j,i]/a[i,i]
            a[j,i:] -= (lam * a[i, i:])
            b[j] -= lam * b[i]

    b = b.astype(float)
    b[len(a)-1] = (b[len(a)-1]/a[len(a)-1,len(a)-1])
    for i in range (len(a)-2, -1, -1):
        b[i] = (b[i] - np.dot(a[i,i+1:],b[i+1:]))/a[i,i]       
    
    return a,b



def getGreatestRelativeRow(a, startingIndex):
    
    j = startingIndex
    
    maxIndex = j
    maxV = a[j,j]/max(a[j,])
    
    for i in range(j+1, len(a)):
        if a[i,j]/max(a[i,]) > maxV:
            maxV = a[i,j]/max(a[i,])
            maxIndex = i
    return maxIndex
    

def swapRows(a, rowOne, rowTwo):    

    row = np.copy(a[rowOne,])
    a[rowOne,] = a[rowTwo,]
    a[rowTwo,] = row
    
    


if __name__ == '__main__':
    a = np.array([[1,2,3],[9,5,6],[7,8,9]])
    b = np.array([43,5,23])
    x, y = gausspivot(a, b)
    
    print(np.linalg.det(a))
    print(np.linalg.cond(a))
    
    a[1,1] = 9.2
    print(np.linalg.cond(a))
    


