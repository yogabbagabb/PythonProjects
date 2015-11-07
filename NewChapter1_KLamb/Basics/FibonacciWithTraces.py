'''
Created on Oct 15, 2015

@author: ahanagrawal
'''
from __future__ import print_function

if __name__ == '__main__':
    
    def fib(n, margin):
        
        space = " " * margin
        print(space, n-1, n-2)
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1;
        
        first = fib(n-1, margin + 4)
        second = fib(n-2, margin + 4)
        print(space, first + second)
        return first + second
    
fib(7,0)