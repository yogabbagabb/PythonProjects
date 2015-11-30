'''
Created on Nov 8, 2015

@author: ahanagrawal
'''
import numpy as np
from OperationsA import gaussElimin


def getLen(numArray):
    t = numArray.shape
    if len(t) <= 1:
        return t[0]
    else:
        return t[0] * t[1]
    
def vandermode(v):
    n = len(v)
    a = np.zeros((n,n))
    for j in range(n):
        a[:,j] = v**(n-j-1)
    return a
        

if __name__ == "__main__":
    a = np.array([[1, 1.2, 1.4, 1.6, 1.8, 2.0]])
    A = np.array([])
    b = np.array([[0,1,0,1,0,1]])
    
    copy = np.zeros((1,6))
    print("Len is " + str(len(a)))
    for i in range(getLen(a)):
        for j in range(getLen(a)):
            copy[0,j] = a[0,i]**(a.size-1-j)
        if (A.size is 0):
            A = np.copy(copy);
        else:
            A = np.append(A, copy, 0)
        print("break_____" + "\n",A)
    print("final")
    print(A)
    print(vandermode(np.array([1, 1.2, 1.4, 1.6, 1.8, 2.0])))
    
    x = gaussElimin(A, b.T)
#     print(A)
    print(x)

#     x = gaussian_elim.GEPP(A, b.T)
    for i in range(6):
        print(np.dot(A[i,:],x))   
    

        
    
    