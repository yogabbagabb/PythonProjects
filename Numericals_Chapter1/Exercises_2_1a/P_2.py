'''
Created on Nov 24, 2015

@author: ahanagrawal
'''
import numpy as np
from OperationsA import gaussElimin
if __name__ == '__main__':
    
    a = np.array([[1,0,0],[1,1,0],[1,5/3,1]])
    b = np.array([[1,2,4],[0,3,21],[0,0,0]])
    
    print(np.linalg.det(a))
    print(np.dot(a,b))
    
    c = np.array([1,2,5])
    x = np.linalg.solve(a, c)
    print(x)
    print(a,c)
    
    print(np.dot(a,x))
    x = gaussElimin(a, c)
    print(x)
    
    print(np.dot(a,x))