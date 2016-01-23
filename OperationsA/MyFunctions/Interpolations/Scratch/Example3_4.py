'''
Created on Jan 22, 2016

@author: ahanagrawal
'''

from OperationsA.MyFunctions.Interpolations import newt
import math


def drange(start, end, step):
    a = start
    while (a <= end):
        yield a
        a += step

if __name__ == '__main__':
    func = lambda a: a + 3
    x = [0.15, 2.30, 3.15, 4.85, 6.25, 7.95]
    y = [4.79867, 4.49013, 4.2243, 3.47313, 2.66674, 1.51909]
    fActual = lambda x: 4.8*math.cos(math.pi*x/20.0)
    
    for a in drange(0.0, 8.1, 0.5):
        print(newt.returnPol(x, func , a, y), " as opposed to ", fActual(a))