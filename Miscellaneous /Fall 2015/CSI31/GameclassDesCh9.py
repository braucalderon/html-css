import random 
from random import *
 # randrange build in fuction give a whole random number
 # random build in fuction give a number with decimal 

def main():
    print_intro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)

# Input: none!
# Output: Print out an introduction to user
def print_intro():
    print ('We are going to simulate a game')

# Input: none
# Output: Ask user foor number games
#   and serving prcentage of both players.
#   then output these 3 numbers 
def getInputs():
    n = eval(input('How many games to simulate?'))
    probA = eval(input('Serving precentage of the first player? '))
    probB = eval(input('Serving percentage of the second player? '))
    

    return probA, probB, n 


# Input: Number games (n), serving percentages of both players
# Output: Number of wins per player as a result of simulating n games
def simNGames(n, probA, probB):

    winsA = 0
    winsB = 0

    for i in range (n):
        scoreA, scoreB = simoneGame (probA, probB)
        if scoreA == 25:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
            
    return winsA, winsB

def simoneGame (probA, probB):
    scoreA, scoreB = 0, 0
    serving = 'A' # either 'A' or 'B' in general
    
    
    while GameNotOver(scoreA, scoreB):
        if serving  =='A':
            if random() < probA:
                scoreA = scoreA + 1
                #print ('A won') #temporary
            else:
                serving = 'B'
        else:
            if random() < probB:
                scoreB = scoreB + 1
                #print ('B won') #temporary
            else:
                serving = 'A'
                
    return scoreA, scoreB

def GameNotOver (scoreA, scoreB):
    return (scoreA < 25 and scoreB < 25 )

# Input: NUmber of games, number of wins for each player
# Output: Prints summary. 
def printSummary(n, winsA, winsB):
    print ('Total number games: ', n)
    print ('Player 1 wins: ', winsA)
    print ('Player 2 wins: ', winsB)
    
