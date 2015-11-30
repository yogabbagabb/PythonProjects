'''
Created on Nov 24, 2015

@author: ahanagrawal
'''

import numpy as np
import scipy.linalg as sp

if __name__ == '__main__':
    a = np.array([[-3,6,-4],[9, -8, 24], [-12, 24, -26]])
    b = np.array([-3, 65, -42])
    
    c = sp.lu_factor(a)  # @UndefinedVariable
    print(c)
    d = sp.lu_solve(c, b)  # @UndefinedVariable
    print(d)
    