'''
Created on Dec 17, 2015

@author: ahanagrawal



Accepts a user-provided function that returns one output for every one input. Finds either the minimum or
maximum of the function, depending on the choice of the boolean parameter findMin, between the parameters a and b.
a and b must contain a minimum between them. To identify a bound guaranteed to contain a minimum near some x, see bracket().
tol defines the tolerance, the desired spacing between two locations where the minimum occurs
'''

from math import sqrt
from math import fabs
from operator import gt
from copy import deepcopy
import numpy as np
def bracket (func, x, findMinimum, stepSize = 0.001):
    
# Determine which direction is downward
    increment = 0.001
    
    
    if findMinimum is True:
        f = lambda x: func(x)
    else:
        f = lambda x: func(x) * -1
        
    if f(np.add(x, stepSize)) > f(x):
        stepSize *= -1
        increment *= -1
    
    pointer = np.add(x ,stepSize)
    previousPointer = x
    while(f(pointer) < f(previousPointer)):
        previousPointer = deepcopy(pointer)
        pointer += stepSize
        stepSize += increment
    
    a = pointer if min(np.linalg.norm(pointer), np.linalg.norm(previousPointer)) == pointer else previousPointer
    b = pointer if a == previousPointer else previousPointer
    
    return a,b

def gold(func, x, findMin, tol = 0.00000001, stepSize = 0.001):
    a,b = bracket(func, x, findMin, stepSize)
    return goldSearch(func, a, b, findMin, tol, stepSize)

def goldSearch(func, a, b,findMin, tol,stepSize = 0.001):
    
    
    R = (sqrt(5)-1)/2
    
    x0 = np.subtract(b,np.multiply(R,(np.subtract(b,a))))
    x1 = np.add(a,np.multiply(R,np.subtract(b,a)))
    
    
    while (np.linalg.norm(np.subtract(x1,x0)) > tol):
        
        if (func(x0) < func(x1)):
            b = x1
            x1 = x0
            x0 = np.subtract(b,np.multiply(R,(np.subtract(b,a))))
            
        else:
            a = x0
            x0 = x1
            x1 = np.add(a,np.multiply(R,np.subtract(b,a)))
        
    return np.divide(np.add(x0,x1),2)    
            
def testFunction(x):  
    return x**2
    
if __name__ == "__main__":
    
    print(bracket(testFunction, 0, True, 0.1))
    a = goldSearch(testFunction, -1, 1, True, 0.00000001)
    
    print(a)
    
    