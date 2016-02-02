'''
Created on Jan 31, 2016

@author: ahanagrawal
'''

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

if __name__ == '__main__':
    frequency = []
    file = open("ModernRecordings.txt", 'r')
    
    for i in range(4):
        container = file.readline().split()
        frequency.append(container)
    print(frequency)
    
# [np.array(frequency[0]).astype(np.float), np.array(frequency[1]).astype(np.float), np.array(frequency[2]).astype(np.float), np.array(frequency[3]).astype(np.float)]    
    n,bins, patches = plt.hist([np.array(frequency[0]).astype(np.float), np.array(frequency[1]).astype(np.float), np.array(frequency[2]).astype(np.float), np.array(frequency[3]).astype(np.float)], 12, normed=1)
    
    mean = np.mean(np.array(frequency[0]).astype(np.float))
    dev = np.std(np.array(frequency[0]).astype(np.float))
    y = mlab.normpdf(bins, mean, dev)
    plt.plot(bins, y, 'r--')
    print(y)
    
    
    plt.subplots_adjust(left=0.15)
    plt.show()