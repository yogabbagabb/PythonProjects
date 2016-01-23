'''
Created on Jan 22, 2016

@author: ahanagrawal
'''

import numpy as np

def nev(yData, xData, x):
    a = yData.copy()
    
    aLength = len(xData)
    
    for k in range(1, aLength):
        a[0:aLength - k] = (a[0: aLength - k] * (xData[k: aLength] - x) + a[1: aLength - k + 1] * (x - xData[0:aLength - k])) / (xData[k: aLength] - xData[0: aLength-k])
        
    return a[0]

if __name__ == '__main__':
    x = np.array([-0.06604, -0.02724, 0.01282, 0.05383])
    y = [4.0, 3.9, 3.8, 3.7]
    
    print(nev(y, x, 0))
    
    ''' should be around 3.8317'''