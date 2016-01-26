'''
Created on Jan 16, 2016

@author: ahanagrawal
'''

from OperationsA.MyFunctions.Powell import powell
import scipy.optimize as sp

if __name__ == '__main__':
    pass

def testFunction(a):    
    return 100*(a[1] - a[0]**2)**2 + (1 - a[0])**2
    
    
if __name__ == '__main__':
    a = [[0 for x in range(2)] for x in range(2)]
    print(a)
    dimensions = 2
    startingPoint = [-1, 1]
    print(powell(1, a, startingPoint, testFunction, dimensions))
    z = sp.minimize(testFunction, startingPoint, (), 'Powell')
    print(z.x)