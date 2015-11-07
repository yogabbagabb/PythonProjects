'''
Created on May 6, 2015

@author: ahanagrawal
'''
import pickle

if __name__ == '__main__':
    
    file = open("new.txt",'wb')
    closet = ["shoe", "giraffe", "chickenn",4]
    
    for item in closet:
        pickle.dump(item,file)
        
    file.close()
    
    lyst = list()
    secFile = open("new.txt", 'rb')
    
    while True:
        try:
            thing = pickle.load(secFile)
            lyst.append(thing)
        except EOFError:
            secFile.close()
            break
    print(lyst)