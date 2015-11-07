'''
Created on May 3, 2015

@author: ahanagrawal
'''


class approximate():
    
    def __init__ (self,iterations):
        self.iterations = iterations
        self.sum = 0        
        
    def approx (self):
    
        for iter in range(0, self.iterations, 1):
            self.sum += (-1)^(iter)* (1/(1+2*iter))
        
    def returnAp(self):
        return self.sum
        
def main():
    
    run = approximate(input("give me your iteration count"))
    run.approx()
    print run.returnAp()
    
    
main()
        