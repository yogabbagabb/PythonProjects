'''
Created on Jan 30, 2016

@author: ahanagrawal
'''

from MCM import InfoSpread as mo
from MCM import FacebookNetwork as f
import numpy as np


if __name__ == '__main__':
    
    channels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    randomness = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    sensitivity = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    timePeriodAverage = np.zeros((len(channels),len(sensitivity)), dtype = object)
    N,x = f.constructMatrix("107.edges")
    print(len(N))
    trials = 100

    for i in range (8,len(channels)):
        for m in range(8,len(sensitivity)):
         
            total = 0
            for j in range(trials):
                neighborList = [0]
                time = mo.runMessage(N, sensitivity[m], channels[i], 0, neighborList)
                total = total + time 
                f.resetFacebookMatrix(N)
                
            timePeriodAverage[i][m] = total/trials
               
 
    
    print(timePeriodAverage)