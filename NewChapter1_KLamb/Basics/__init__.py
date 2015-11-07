from __future__ import  print_function
import math
import random

from __builtin__ import list
from _random import Random


print(dir(tuple))

hello = (2,3,4)
hello += (4,5)
''' tuples are immutable, yet they can be concatenated to? In likelikhood, the contatentation process
probably returns another tuple'''

print (hello)

random.seed(3)



list = []
list.append(3)
for i in range(1,10):
    list.append(i* random.random())

print(list)
isSorted = False

while not isSorted:

    count = 0;
    isSorted = True;
    while count < len(list)-1:      
        if (list[count+1] < list[count]):
            isSorted = False;
            temp = list[count]
            list[count] = list[count+1]
            list[count+1] = temp
        print(count)        
        count += 1
            
print(list)
            
    
