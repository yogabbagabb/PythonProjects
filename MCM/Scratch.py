'''
Created on Jan 31, 2016

@author: ahanagrawal
'''



import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

if __name__ == '__main__':
#     f = open("ModernRecordings.txt", 'w')
#     list = [1,2]
#     f.write("1")
#     f.write("2")
#     f.write("\n")
#     f.write("3")
    
        
#         a = [6,4,5]
#         a.sort(key=None, reverse=False)
#         print(a)    

    print()

    
    # example data
    mu = 100  # mean of distribution
    sigma = 15  # standard deviation of distribution
    x = mu + sigma * np.random.randn(10000)
    b = mu + sigma * np.random.randn(10000)
    
    num_bins = 50
    # the histogram of the data
    n, bins, patches = plt.hist([x,b], num_bins, normed=1)
    print(x,n,num_bins,bins,patches)
    # add a 'best fit' line
#     y = mlab.normpdf(bins, mu, sigma)
#     plt.plot(bins, y, 'r--')
#     plt.xlabel('Smarts')
#     plt.ylabel('Probability')
#     plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
#     
    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.show()