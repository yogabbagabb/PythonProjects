'''
Created on Oct 19, 2015

@author: ahanagrawal
'''

from __future__ import print_function




class Counter(object):
    def __init__(self):
        self.moron = 2;

def doSomething (count):
    count.moron = 3;
    
i = Counter()

print(i.moron)

doSomething(i)
print(i.moron)