'''
Created on Oct 24, 2015

@author: ahanagrawal
'''
from NewChapter1_KLamb.PokemonGame import Player

if __name__ == "__main__":
    
    Player.manufactureLists()
    l = list()
    for i in range(0,5):
        for j in range(0,4):
            l.append(Player("F"));
            print ("Trial #" + j+1 , l[j].getList())
        print("\n")
        l = list()
            