'''
Created on Oct 18, 2015

@author: ahanagrawal
'''

from NewChapter1_KLamb.PokemonGame.MoveEntry import MoveEntry
from _random import Random
from random import Random



class Player():
    
    #class variables
    moveA = [MoveEntry(move="Scratch", points=-30), MoveEntry(move="Chew", points = -3)]
    moveB = ["Jump", "Scream", "Howl", "Be"]
    moveC = ["Burp", "Chew", "Spit", "Crawl"]
    moveD = ["Scratch", "Chew", "Spit", "Crawl"]
    moveArray = [moveA, moveB,moveC,moveD]
    usedMoveArrayIndices = set()
    
    def __init__ (self, name):
        self.name = name
        self.health = 100
        self.assignList()

    def getHealth(self):
        return self.health
    
    def suffer(self, d):
        if self.health - d != 0:
            self.health -= d;
        else:
            self.health = 0;
        
    def fromPeople (self, **kwargs):
        self.__dict__.update(kwargs)
        self.assignList()
        
    def assignList (self):
        if len(Player.usedMoveArrayIndices) == 4:
            Player.usedMoveArrayIndices.clear()
            
        rand = Random()
        randomValue = int(rand.random() * 4)
    
        while Player.usedMoveArrayIndices.__contains__(randomValue):
            randomValue = int(rand.random() * 4)
        
        Player.usedMoveArrayIndices.add(randomValue)
        self.moves = Player.moveArray[randomValue]

    @staticmethod
    def manufactureLists():
#         for i in range(0,Player.moveB.len()):
#             Player.moveB.(i) = MoveEntry.MoveEntry(move=i,points = 100)

        rand = Random() 
        
        for i in range (0,len(Player.moveArray)):
            tempL = Player.moveArray[i]
            for j in range(0,len(tempL)):
                tempL[j] = MoveEntry(move=tempL[j], points = 100*rand.random())
               
            
    def printList(self):
        print (self.moves)
        
    def getMoves(self):
        return self.moves
            
    def __hash__(self):
        total = 0
        length = len(self.name)
        for i in range (0,len(self.name)):
            total += ord(self.name[i]) * 32**length-1-i
        return total
    def __eq__ (self, otherP):
        return otherP.name == self.name
    
    
    def __str__ (self):
        return self.name
    
    def __repr__ (self):
        return self.__str__()
     
    
            

if __name__ == '__main__':
    
    x = Player("Bob")
    y = Player("Bobby")
    print(x.moves)
    print(y.moves)
    
    
    
    
    