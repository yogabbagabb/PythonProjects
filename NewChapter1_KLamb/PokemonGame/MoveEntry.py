'''
Created on Oct 18, 2015

@author: ahanagrawal
'''


class MoveEntry (object):
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        
    def getPoint(self):
        return self.points
    def getMove(self):
        return self.move
    
    def str (self):
        return "Move " + str(self.move) + "---> " + str(self.points);
    
    def __repr__(self, *args, **kwargs):
        return self.str()
    
    
if __name__ == "__main__":
    x = MoveEntry(move="scratch",points=3)
    print(x.getMove())
    print(x.getPoint())