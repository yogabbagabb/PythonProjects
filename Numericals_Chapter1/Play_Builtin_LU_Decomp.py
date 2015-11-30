'''
Created on Nov 23, 2015

@author: ahanagrawal
'''

import numpy as np
import scipy.linalg as sp

if __name__ == '__main__':
    
    a = np.array([[1,2,3],[4,5,6],[3,5,6]])
    
    a,b = sp.lu_factor(a)  # @UndefinedVariable
    print(a)
    print(b)
    d = sp.lu_solve((a,b), np.array([1,2,3]))
    print(d)    