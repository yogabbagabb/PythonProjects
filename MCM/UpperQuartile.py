'''
Created on Jan 30, 2016

@author: ahanagrawal
'''

from MCM import InfoSpread as mo
from MCM import FacebookNetwork as f
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


if __name__ == '__main__':
    
    channels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    randomness = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    sensitivity = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    frequency = np.zeros((4,1), dtype = object)
    N,x = f.constructMatrix("107.edges")
    print(len(N))


    file = open("ModernRecordings.txt", 'w')
    
    for i in range (6, len(sensitivity)):
        values = []
        for m in range(6, len(channels)):
         
            
            total = 0
             
            for j in range(70):
                neighborList = [0]
                time = mo.runMessage(N, sensitivity[m], channels[i], 0, neighborList)
                total = total + time 
                values.append(time)
                f.resetFacebookMatrix(N)
                
        values.sort(key=None, reverse=False)
        frequency[i-6][0] = values
        
        for entry in range(len(values)):
            file.write(str(values[entry]) + " ")
        file.write("\n")
        
    plt.hist([frequency[0][0], frequency[1][0], frequency[2][0], frequency[3][0]], 70, normed=1)
    plt.subplots_adjust(left=0.15)
    plt.show()
    
