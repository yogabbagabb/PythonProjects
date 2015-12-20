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
def bracket (func, x, findMinimum, stepSize = 0.001):
    
# Determine which direction is downward
    increment = 0.001
    
    
    if findMinimum is True:
        f = lambda x: func(x)
    else:
        f = lambda x: func(x) * -1
        
    if f(x+stepSize) > f(x):
        stepSize *= -1
        increment *= -1
    
    pointer = x + stepSize
    previousPointer = x
    while(func(pointer) < func(previousPointer)):
        previousPointer = pointer
        pointer += stepSize
        stepSize += increment
    
    a = min(pointer, previousPointer)
    b = max(pointer, previousPointer)
    
    return a,b

def goldSearch(func, a, b,findMin, tol,stepSize = 0.001):
    
    
    R = (sqrt(5)-1)/2
    
    x0 = b - R*(b-a)
    x1 = a + R*(b-a)
    
    
    while (fabs(x1-x0) > tol):
        
        if (func(x0) < func(x1)):
            b = x1
            x1 = x0
            x0 = b - R*(b-a)
            
        else:
            a = x0
            x0 = x1
            x1 = a + R*(b-a)
        
    return x0,x1    
            
def testFunction(x):  
    return x**2
    
if __name__ == "__main__":
    
    print(bracket(testFunction, 0, True, 0.1))
    a,b = goldSearch(testFunction, -1, 1, True, 0.00000001)
    
    print(a,b)
    
    