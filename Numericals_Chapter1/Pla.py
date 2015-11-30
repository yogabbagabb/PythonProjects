'''
Created on Nov 8, 2015

@author: ahanagrawal
'''
import numpy as np

if __name__ == '__main__':
#    print(np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10,11,12]], axis=1))
#     A = np.array([])
#     a = np.array([1,2,3])
#     b = np.array([4,5,6])
#     c = np.array([7,8,9])
#     
#     A = np.append(A,a,0)
#     A = np.concatenate((A,b),axis = 0)
#     print(A)

    a = np.zeros((3,3))
    
    count = 0
    for i in range(3):
        a[:,i] = count
        count += 1
        
    print(a)
        