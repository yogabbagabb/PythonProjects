from __future__ import print_function

'''
Created on Oct 6, 2015

@author: ahanagrawal
'''

i = 0
while i < 10:
    j = input("Give me a number")
    for num in range(0,4):
        for secondNum in range(0,j):
            print("%1s%-1s" % ("*", "*"), end = "")
        print("\n")
    j -= 1;
    
        




