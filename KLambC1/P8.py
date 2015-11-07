'''
Created on May 6, 2015

@author: ahanagrawal
'''




class NavLine():
    '''
    classdocs
    '''


    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.list = list()
        file = open(fileName,'r')
        
        for line in file:
            self.list.append(line)
            
            
        print(self.list)
           
            
    
    def displayLine(self, index):
        return self.list[index]
    
        
def good():

    if __name__ == "__main__":        
        navigator = NavLine("new.txt")    
        
        choice = input("Enter a number! 0 to switch off")
    
        if choice == 0:
            print "sayonara"
        
        else:
            print navigator.displayLine(choice)
            good()

        
good()
    
            
