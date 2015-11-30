'''
Created on Nov 29, 2015

@author: ahanagrawal
'''

import numpy as np
import scipy.linalg as linalg

def constructArray(aList):
    
    arr = np.zeros((len(aList),len(aList)))
    barr = np.zeros((len(aList),))
    barr = barr.T
   
    
    index = 0

    for i in range(0,len(aList)):
        firstNum = aList[int(i)].__getitem__(0)
        secondNum = aList[int(i)].__getitem__(1)
        
        arr[index,0] = 1
        for j in range(1, len(aList)):
            
            arr[index,j] = firstNum **  j
        barr[index] = secondNum
        
        index = index + 1
    
    return arr,barr

   
    
#     function is a_0 + xa_1 + a_2x^2 + a_3x^3


if __name__ == '__main__':
    lyst = [(0,10),(1,35),(3,31),(4,2)]
    
    a,b = constructArray(lyst)
    
    lu,p = linalg.lu_factor(a)
    x = linalg.lu_solve((lu, p), b.T)
    
    print(x)