# Deck.py

from random import randrange
from Card import Card
from random import shuffle
  
class Deck():

    #------------------------------------------------------------

    def __init__(self):
        

        """post: Creates a 52 card deck in standard order"""

        cards=[]
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                  cards.append(Card(rank,suit))
        self.cards = cards
        self.size = len(self.cards)         # to keep track of the current size, using instance variable 
        


    #------------------------------------------------------------

    def size(self):

        """Cards left
        post: Returns the number of cards in self"""

        return self.size

    #------------------------------------------------------------

    def deal(self):

        """Deal a single card
        pre:  self.size() > 0
        post: Returns the next card, and removes it from self.card if
        the deck is not empty, otherwise returns False"""

        if self.size > 0:
            return self.cards.pop()
        else:
            return False

    #------------------------------------------------------------

    def shuffle(self):

        """Shuffles the deck
        post: randomizes the order of cards in self"""

        
        
        shuffle(self.cards)

        
##        for i,card in enumerate(cards):
##            pos = randrange(i,n)
##            cards[i] = cards[pos]
##            cards[pos] = card

    #------------------------------------------------------------

    def AddBottom(self,card):
        

        """ Add a card at the end of the list"""
        
        
        self.cards.append(card)
        self.size += 1


    #------------------------------------------------------------

    def AddTop(self,card):
        """ Add a card at the top of the deck"""

        
        self.cards.insert(0,card)
        self.size += 1
    


    #------------------------------------------------------------

    def AddRandom(self):
        """Add a card somewhere within the deck"""

        
        self.cards.insert(randit(0,self.deck_size - 1))
        self.size += 1

    
    
        
        

        
        
