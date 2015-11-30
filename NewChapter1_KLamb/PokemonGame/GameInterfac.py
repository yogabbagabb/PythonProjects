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
        print("Player " , index + 1 , " is up with health ", playerList[index].getHealth(), end = "\n")
        print("It has moves" , playerList[index].getMoves())
        ''' find  a way to append a message onto the prompt displayed using input''' 
        prompt = "Choose an index of the move you'd like to use from 1-" + str(len(playerList[index].getMoves()))
        move = int(input(prompt))
        print(playerList)
        prompt = "And then choose the opponent you would like to attack from 1-" + str(len(playerList)) + "amongst" + str(playerList)
        opponent = int(input(prompt))
        dealDamage(playerList[index], move-1, playerList[opponent-1])
        updatePlayerList()
        count += 1
        
    print("Game Over: ", playerList , " wins!" )


def updatePlayerList():
    i = 0
    while i < len(playerList):
        try:
            if playerList[i].getHealth() <= 0:
                del playerList[i]
                
            else:
                i+= 1
        except IndexError:
            print("index:", i)
def dealDamage(playerInstance, moveIndex, opponent):
    moves = playerInstance.getMoves()
    opponent.suffer(moves[moveIndex].getPoint())
    
if __name__ == "__main__":
    execute();