'''
Created on Nov 23, 2015

@author: ahanagrawal
'''

import numpy as np

if __name__ == "__main__":
    a = np.array([[1,2,3],[2,3,4],[3,4,5]])
    print(np.linalg.det(a))
    x = np.linalg.solve(a,np.array([2,3,4]))
    print(x)
    a = np.array([[1.1,2.1,3.1],[2,3,4],[3,4,5]])
    print(np.linalg.det(a))
    print(np.linalg.norm(a))

#Ill Conditioning occurs when the determinant's magnitude is very far off from the magnitude of, say, the average
# matrix element 
    
    x = np.linalg.solve(a,np.array([2,3,4]))
    print(x)
    
    
    b = np.array([[2.11,-0.80,1.72],[-1.84, 3.03, 1.29],[-1.57, 5.25, 4.30]])
    print(np.linalg.norm(b))


