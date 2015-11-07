'''
Created on Oct 15, 2015

@author: ahanagrawal
'''
from __future__ import print_function

if __name__ == '__main__':
    dict = {}
    dict[2] = 3
    dict[3] = 2
    dict[2] = 4
    print(dict)
    
    print(dict.pop(1,4))
    print(dict)
    dict.get(2);
    print(dict)
    
# this might as well give me the technique of using a map