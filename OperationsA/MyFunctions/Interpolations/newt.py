'''
Created on Jan 20, 2016

@author: ahanagrawal
'''


'''
A two dimensional interpolation scheme that uses newton's divided difference
approach

The one dimensional matrix passed should contain all evaluations of 
f(x) for all x of interest
'''


def makeCoefficients(a, x):
    
    length = len(a)
    
    for k in range(1, length):
        for i in range(k, length):
            a[i] = (a[i] - a[k-1])/(x[i] - x[k-1])
    
def returnPol(x, func, xD):
    
    a = [func(x[i]) for i in range (len(x))]
    makeCoefficients(a, x)
    
    polDegree = len(x) - 1
    
     
    p = a[polDegree]
    
    for i in range (1, len(x)):
        p = a[polDegree - i] + (xD - x[polDegree - i])*p
    
    return p

if __name__ == '__main__':
    pass