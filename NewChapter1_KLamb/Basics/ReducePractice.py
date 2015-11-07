'''
Created on Oct 17, 2015

@author: ahanagrawal
'''

import functools

if __name__ == '__main__':
    
    sum =functools.reduce(lambda x, y: x + y, range(1,6))
    print sum