'''
Created on Oct 22, 2015

@author: ahanagrawal
'''
from __future__ import print_function
from NewChapter1_KLamb.PokemonGame.Player import Player

if __name__ == "__main__":
    x = set()
    x.add(Player("Bob"))
    x.add(Player("joe"))
    print(x)
    print(len(x))
    print(0)
    x.add(Player("Bob"))
    
    print(x)


