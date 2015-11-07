'''
Created on May 6, 2015

@author: ahanagrawal
'''

if __name__ == '__main__':
    
    
    
    file = open("new.txt", 'w')
    for g in range(0,100,2):
        file.write(str(g) +  "\n")
     
    file.close()
    sum = 0
     
    reader = open("new.txt",'r')
    for line in reader:
#         for word in line.split():
        sum += int(line)
         
    print sum
    
#     
    
    
#     file = open("new.txt",'w')
#     file.write(" good old chap \n bad old chap")
#     
#     for gna in range(0,100):
#         number  = gna
#         file.write(str(number) + "\n")
#         
#     file.close()
#     
#         
#     
#     bro = open("new.txt", 'r')
#     string = bro.read()
#     print (string)
#     print ("End OF C1")
#     
#     ca = open("new.txt",'w')
#        
#     for var in range(0,100,2):
#          ca.write(str(var))
#                        
#     for line in bro:
#       print(line)
#             
#         
#     while True:
#         text = bro.readline()
#         if text == "":
#              break
#         print(text)
            
