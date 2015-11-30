'''
Created on Nov 26, 2015

@author: ahanagrawal
'''

import numpy as np
import scipy.linalg as ln

def getOne(size):
    
    a = np.zeros((size,size))

    for i in range(size):
        for j in range(size):
            a[i,j] = 1/(i+j+1)
            
    b = np.zeros(size)
    
    for i in range(size):
#         print(np.sum(a[i:]))
        b[i] = np.sum(a[i,:],0)
#     print(a)
        
    lu = ln.lu_factor(a)
    b = ln.lu_solve(lu, b)
    
    return b


if __name__ == '__main__':
    for i in range(1,10,1):
        b = getOne(i)
        for j in range(len(b)):
            if (abs(b[j] - 1) > 0.000001):
                print(i-1, " is the last time when the value is close to 1")
                break
                
    
    
