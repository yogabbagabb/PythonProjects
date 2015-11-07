'''
Created on Oct 16, 2015
@author: ahanagrawal
'''

import random

if __name__ == '__main__':
    
    
    gradesList = [];
    for i in range(10):
        if random.random() < 0.5:
            gradesList.append(0)
        else:
            gradesList.append(10)
    print(gradesList)
    def isNotZero(entry):
        if (entry == 0):
            return False;
        else:
            return True;
        

    newList = filter(isNotZero, gradesList)
    print(newList);