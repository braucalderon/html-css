# main1.py

from Deck import Deck
from Player import Player
from Card import Card 
from random import *
import time

def main():

    '''
    Creates the hard of the game by using the classes
    
    pre: creates the players, the counts and the cards by calling each class respectibly.
    post: compare the cards based in the game rules and print the results
        by names and numbers. 

    '''
    line = '\n#########################################\n'
    separation = '__________________________________\n'
    
    print(line)
    n=input("Enter Player 1: ").upper()
    n1=input("\nEnter Player 2: ").upper()

    # creates a variable for the class deck
    d1 = Deck()
    d1.shuffle()
            

    print(line)
    print("  ",separation)
    
    # picks a random card from card.suits
    my_random = d1.deal()            
    print ("       The Trump Suit Card is \n")
    print("          ",my_random,'\n')
    print("     The Deck starts with 51 Cards")
    print("  ",separation)
    print(line)
    
 

    # creates a new variable for the name input by the user into the class player
    player1 = Player(n)         
    player2 = Player(n1)


    # assign variables from the class card for easy acess later into the program
    rank = Card.RANKS           
    suit = Card.SUITS
    
    
    
    # rounds are eequals to the 26 times 
    rounds = 1
    
    # created two variables for later use in the final result, keeps track of the
    # winner and loser separately from the points in the class player
    card1 = 0
    card2 = 0
    total = 51

 
 
    while rounds < 26:

        
        r="                              Round: "
        d="                          Card Deck: "
        ctotal ="Total Cards: "
        w = " Won this turn"
        totalcards1 = player1.get_value()   # creates a variable for easy access later in the program
        totalcards2 = player2.get_value()
        
        turn_1 = d1.deal()  # creates a new variable using a variable from Deck()
        turn_2 = d1.deal()
        
        
        
        print (line)
        print (r,rounds)
        total -= 2
        print(player1.get_name(), " has ", turn_1)
        print(player2.get_name(), " has ", turn_2)
        print(d,total)
        

        rounds += 1
        # compare if both variables suit() are equal bu not equal to the trump card
        if (turn_1.suit() == turn_2.suit() and
        turn_1.suit() != my_random.suit() and
        turn_2.suit() != my_random.suit()):
            

            if (turn_2.rank() > turn_1.rank()):
                
                print(separation) 
                print (player2.get_name(), w)       
                print(ctotal, totalcards2)
                player2.set_value()
                card2 += 2
                time.sleep(1)
            
            else:
                print(separation)
                print (player1.get_name(), w)
                print(ctotal, totalcards1)
                # set the value to be printed
                player1.set_value()
                card1 += 2
                time.sleep(1)

        if (turn_1.suit() == turn_2.suit() and
        turn_1.suit() == my_random.suit() and
        turn_2.suit() == my_random.suit()):

            print(separation)
            print("Both Players Won this Turn \n")
            print (player1.get_name(), 'with ',totalcards1-1, " Cards")
            player1.set_value()
            print (player2.get_name(), 'with ', totalcards2-1, " Cards")
            player2.set_value()
            card1 += 1
            card2 += 1
            time.sleep(1)
            

        
        # 1.compare if the player has the trump card
        if (turn_1.suit() == my_random.suit() and
        turn_2.suit() != my_random.suit()):
            
        
            print(separation) 
            print (player1.get_name(), w)       
            print(ctotal, totalcards1)
            player1.set_value()
            card1 += 2
            time.sleep(1)
            
        # same as 1 
        if (turn_2.suit() == my_random.suit() and
        turn_1.suit() != my_random.suit()):

            print(separation) 
            print (player2.get_name(), w)       
            print(ctotal, totalcards2)
            player2.set_value()
            card2 += 2
            time.sleep(1)
            
        # compare for inequailty of cards
        if (turn_2.suit() != turn_1.suit() and
        turn_2.suit() != my_random.suit() and
        turn_1.suit() != my_random.suit()):
            
            print(separation)
            print ("Don't get lost in the shuffle \n"
                   "     No winner this turn")
            # take one points (card) from each player
            time.sleep(1)
            


        # once the deck is empty at 26, prints the winner and the loser
        if rounds == 26:
            
            print(line)

            # compare points from the variables created in the while loop
            if card1 == card2:
                print("   ",separation)

                print("     Life is like a game of cards.\n"
                      "\n        The Game was a Match.")
                print("   ",separation)
                
                print("          ",player1.get_name()," has", card1+1, "Cards\n")
                print("          ",player2.get_name()," has", card2+1, "Cards")
                print("   ",separation)
                print(line)
                break
                
                

            if card2 > card1:

                print("            The Winner is\n"
                      "\n                ",player2.get_name(),)
                
                print("   ",separation)
                print ("   ",player2.get_name()," won this game by ", card2, "Cards.\n")

            else:
                print("            The Winner is\n"
                      "\n                ",player1.get_name())
                print("   ",separation)
                
                print ("   ",player1.get_name()," won this game by ", card1, "Cards.\n")
                

               

            if card1 < card2:
                
                print ("   ",player1.get_name()," lost this game by ", card1, "Cards.\n")

            else:
                
                print ("   ",player2.get_name()," lost this game by ", card2, "Cards.\n")
                
            print("   ",separation)
            print(line)
                
            
                
                

                
"""
Side effect:

variables card1 and card2 were created because due to the if == 27
statement. The results for the  winner and the loser were not  printed
accurate, it was a difference by +2 points for one player when both were
printed using the class player.
But it was not the same case when only the winner was printed using the
class player, the result was accurate at all times. 

"""


main()

    

    

    

    
