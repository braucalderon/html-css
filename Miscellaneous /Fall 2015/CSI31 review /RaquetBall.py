import random
from random import *

def main():
    print_intro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n,probA,probB)
    printSummary(n, winsA, winsB)

# Input: none!
# Ouput: Print out an introduction to user
def print_intro():
    print("We are going to simulate a series of raquetball games. You will now be asked for some info.")

# Input: none
# Ouput: Ask user for number games,
#        and serving percentages of both
#        players.
#        Then output these 3 numbers.
def getInputs():
    n = eval(input("How many games to simulate? "))
    probA = eval(input("Serving percentage of first player? "))
    probB = eval(input("Serving percentage of second player? "))
    return probA, probB, n

# Input: Number games (n), serving percentages
#        of both players
# Output: Number of wins per player as a
#         result of simulating n games
def simNGames(n,probA,probB):

    winsA = 0
    winsB = 0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA == 15:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A" # Either "A" or "B" in general
    
    while GameNotOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A" 
        
    
    return scoreA, scoreB

def GameNotOver(scoreA, scoreB):
    return(scoreA < 15 and scoreB < 15)


# Input: Number of games, number of wins for
#        each player
# Output: Prints summary
def printSummary(n, winsA, winsB):
    print("Total number games: ", n)
    print("Player 1 wins: ",winsA)
    print("   with percent:", 100*(winsA/n)) 
    print("Player 2 wins: ",winsB)
    print("   with percent:", 100*(winsB/n)) 





