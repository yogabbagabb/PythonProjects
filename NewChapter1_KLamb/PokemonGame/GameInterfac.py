'''
Created on Oct 24, 2015

@author: ahanagrawal
'''
from __future__ import print_function

from NewChapter1_KLamb.PokemonGame import Player

p = Player
playerList = list()

def execute():
    Player.manufactureLists()
    playerNumber = input("How many players do you want? \n")
    for i in range(0,int(playerNumber)):
        name = input("His name?")
        playerList.append(p(name))
        
    count = 0
    while (len(playerList) > 1):
        index = count%len(playerList)
        print("Player " , index , " is up", end = "\n")
        print("It has moves" , playerList[index].getMoves())
        ''' find  a way to append a message onto the prompt displayed using input''' 
        prompt = "Choose an index of the move you'd like to use from 1-" + str(len(playerList[index].getMoves()))
        move = int(input(prompt))
        print(playerList)
        prompt = "And then choose the opponent you would like to attack from " + str(playerList)
        opponent = int(input(prompt))
        dealDamage(playerList[index], move, playerList[opponent-1])
        updatePlayerList()
        count += 1


def updatePlayerList():
    for i in range(len(playerList)):
        if playerList[i].getHealth() == 0:
            del playerList[i]
            i-= 1
def dealDamage(playerInstance, moveIndex, opponent):
    moves = playerInstance.getMoves()
    opponent.suffer(moves[moveIndex-1].getPoint())
    
if __name__ == "__main__":
    execute();