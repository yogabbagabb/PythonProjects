'''
Created on Jan 26, 2016

@author: ahanagrawal
'''

from OperationsA.MyFunctions.Matrices import trisolve

def getK(x, y):
    n = [[0 for i in range (len(x) - 2)] for i in range(len(x) - 2)]
    b = [0 for i in range(len(x) - 2)]
    
    index = 0
    
    for i in range (1, len(n) + 1):
        originalIndex = index
        if (i - 1 != 0): 
            n[i-1][index] = x[i - 1] - x[i]
            index += 1
        n[i-1][index] = 2*(x[i - 1] - x[i + 1])
        index += 1
        if (i + 1 != len(n)+1):
            n[i-1][index] = x[i] -  x[i + 1]
            index += 1
        
        if (i != 1):
            index = originalIndex + 1
        else:
            index = 0    
            
        b[i-1] = 6 * ((y[i-1] - y[i])/(x[i-1] - x[i]) - (y[i] - y[i+1])/(x[i] - x[i+1]))
        
    k = trisolve(n, b)
    print(n)    
    print(b)
    print(k)
    
    kGood = [0 for x in range(len(k) + 2)]
    kGood[1: len(k) + 1] = k[0: len(k)]

    return kGood
    
    
def cubeSpline(xData, yData, k, x):
    i = 0
    j = len(xData) - 1
    
    while (j - i > 1):
        mid = int((i + j)/2)
        if (x > xData[mid]):
            i = mid
        else:
            j = mid
            
    h = xData[i] - xData[i+1]
    
    y = k[i]/6*((x-xData[i+1])**3/h - (x - xData[i+1])*h) 
    - k[i+1]/6*((x-xData[i])**3/h - (x - xData[i])*h) 
    + (yData[i]*(x - xData[i+1]) - yData[i+1]*(x - xData[i]))/h
    
    return y


if __name__ == '__main__':
    x = [1.0,2.0,3.0,4.0,5.0]
    y = [0.0,1.0,0.0,1.0,0.0]
    k = getK(x, y)
    a = cubeSpline(x, y, k, 1.5)
    print(a)