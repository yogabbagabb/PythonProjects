'''
Created on Feb 1, 2016

@author: ahanagrawal
'''
import matplotlib.pyplot as plt





if __name__ == '__main__':
#     f = open("retweet.edgelist")
#     line = f.readline()
#     array = []
#     
#     while (line != ""):
#         lineArray = line.split()
#         array.append(lineArray[4])
#         line =  f.readline()
#     
#     array.sort()
#     
#     first = array[0]
#     g = open('Sorted.txt','w')
#     
#     for i in range(0,len(array)):
#         g.write(str(int(array[i]) - int(first)))
#         g.write('\n')
    
    
    f = open("Sorted.txt", 'r')
    line = f.readline()
    array = []
    start = 0
    count = 0
    index = 0
    while (line != "" and index < 20):
        num = int(line)
        
        if (num > index * 20000):
            array.append(count)
            index += 1
            count = 0
        count += 1
        
        line = f.readline()
        
    print(array)
    plt.hist(array)
    plt.show()
    
        
        
        