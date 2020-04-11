# main1.py

from Deck import Deck
from Card import Card 
from random import *


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
  #  n=input("Enter Player 1: ").upper()

    # creates a variable for the class deck
    d1 = Deck()
    d1.shuffle()


    pile1=d1.deal()
    pile2=d1.deal()
    pile3=d1.deal()
    pile4=d1.deal()

    a=([pile1,pile2,pile3,pile4]) 

    suit = Card.SUITS
    rank = Card.RANKS

  
    
    
    game=1
 
    for i in range(1,15):
        

       
        
        print("\nGame {}\n".format(game))
        print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
        game+=1

        

    
             
            
        # comparing [0]
        if a[0].rank() == a[1].rank():
            a[0]=d1.deal()
            a[1]=d1.deal()
            
            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            

        if a[0].rank() == a[2].rank():
            a[0]=d1.deal()
            a[2]=d1.deal()
            
            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            
            

        if a[0].rank() == a[3].rank():
            a[0]=d1.deal()
            a[3]=d1.deal()
            
            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            
        

        # comparing [1]
        if a[1].rank() == a[0].rank():
            a[1]=d1.deal()
            a[0]=d1.deal()
            
            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            
        

        if a[1].rank() == a[2].rank():
            a[1]=d1.deal()
            a[2]=d1.deal()
            

            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            
        

        if a[1].rank() == a[3].rank():
            a[1]=d1.deal()
            a[3]=d1.deal()
            
            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            
            
        
        # comparing [2]
        if a[2].rank() == a[1].rank():
            a[1]=d1.deal()
            a[2]=d1.deal()
            

            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            

        if a[2].rank() == a[0].rank():
            a[0]=d1.deal()
            a[2]=d1.deal()
            

            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            
        

        if a[2].rank() == a[3].rank():
            a[1]=d1.deal()
            a[3]=d1.deal()
            

            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            

        # comparing [3]
        if a[3].rank() == a[1].rank():
            a[1]=d1.deal()
            a[2]=d1.deal()
            

            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            

        if a[3].rank() == a[0].rank():
            a[0]=d1.deal()
            a[2]=d1.deal()
            

            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")
            
        

        if a[3].rank() == a[2].rank():
            a[2]=d1.deal()
            a[3]=d1.deal()


    
        
            

            print("|",a[0],"|",a[1],"|",a[2],"|",a[3],"|")

    
    
    
  

    print(line)
    print("  ",separation)
    
    
    
'''
    # creates a new variable for the name input by the user into the class player
    player1 = Player(n)         
 

    
    
    # rounds are eequals to the 26 times the player takes cards until the deck is empty
    rounds = 1
    
    # created two variables for later use in the final result, keeps track of the
    # winner and loser separately from the points in the class player
    card1 = 0
 
 
    while rounds < 27:

        
 
        totalcards1 = player1.get_value()           # creates a variable for easy access later in the program
 
        
        turn_1 = d1.deal()                          # creates a new variable using a variable from d1=Deck() from the class deck
 



        # compare if  the suit() variable is equals to turn_1 variable, if so
        if turn_1.suit() == turn_2.suit():          
            
            rounds += 1
            # then compare the both ranks for the highest
            if (turn_1.rank() > turn_2.rank()):
                print(separation) 
                print (player1.get_name(), w)       
                print(ctotal, totalcards1)
                player1.set_value()
                card1 += 2
                time.sleep(1) 
            
            else:
                print(separation)
                print (player2.get_name(), w)
                print(ctotal, totalcards2)
                # set the value to be printed
                player2.set_value()
                card2 += 2
                time.sleep(1)

        # compare the suit() variable for inequality, if so
        if turn_1.suit() != turn_2.suit():
            
            rounds += 1
            # compare the  highest rank
            if turn_1.rank() > turn_2.rank():
                print(separation)
                print (player1.get_name(), w)
                print(ctotal, totalcards1)
                player1.set_value()
                card1 += 2
                time.sleep(1)

            elif turn_1.rank() == turn_2.rank():
                print(separation)
                print ("Don't get lost in the shuffle \n"
                       "     No winner this turn")
                # take one points (card) from each player
                (totalcards1-1)
                (totalcards2-1)
                time.sleep(1)
                

            else:
                print(separation)
                print (player2.get_name(), w)
                print(ctotal, totalcards2)
                player2.set_value()
                card2 += 2 
                time.sleep(1)

        # once the deck is empty at 26, prints the winner and the loser
        if rounds == 27:
            
            print(line)

            # compare points from the variables created in the while loop
            if card1 == card2:
                print("   ",separation)

                print("     Life is like a game of cards.\n"
                      "\n        The Game was a Match.")
                print("   ",separation)
                
                print("          ",player1.get_name()," has", card1, "Cards\n")
                print("          ",player2.get_name()," has", card2, "Cards")
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
                
            
                
                
'''
                
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

    

    

    

    
