'''
Created on Nov 15, 2015

@author: ahanagrawal
'''

import numpy as np

def vandermode(a):
    n = len(a)
    v = np.zeros((n,n))
    for j in range(n):
        v[:,j] = a**(n-j-1)
    

    print(v)

if __name__ == "__main__":
    
    a = np.array([1, 1.2, 1.4, 1.6, 1.8, 2.0])
    
    n = len(a)
    v = np.zeros((n,n))
    for j in range(n):
        v[:,j] = a**(n-j-1)
    

    print(v)
    
    print(vandermode(np.array([1, 1.2, 1.4, 1.6, 1.8, 2.0])))