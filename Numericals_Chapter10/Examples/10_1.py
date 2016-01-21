'''
Created on Dec 20, 2015

@author: ahanagrawal
'''

from OperationsA import GoldenSearch as g

def function(x):
    penalty = 0
    if (x < 0):
        penalty = 100
        
    return 1.6*x**3 + 3*x**2 - 2*x + penalty


if __name__ == '__main__':
    
    
    a,b = g.bracket(function, 0, True)
    a,b = g.goldSearch(function, a, b, True, 0.00001)
    print(a,b)