# main1.py

from Deck import Deck
from Card import Card
from random import *

def main():

    n=int(input("Enter the number of cards display: "))

    deck=Deck()
    deck.shuffle()
    rank=Card.RANKS
    

    mycards=[str(deck.deal()) for i in range(n)]

    
    
    rounds = 1

    suits = (['Clubs', 'Diamonds', 'Hearts', 'Spades'])

    rank = (['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                  'Seven', 'Eight', 'Nine', 'Ten', 
                  'Jack', 'Queen', 'King'])

    h=[]
    
    cards = 0
    for i in mycards:
        print("\n||___",i," \n")
        h.append(mycards)
       

        
    if h[0] == suits[0]:
        print("M")
        
    
        
                
    


    
            
            

                
        


    
    
    

    
   
    
main()
