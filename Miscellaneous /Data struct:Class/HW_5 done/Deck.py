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

        return len(self.cards)

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

        n = self.size
        cards = self.cards
        shuffle(cards)

        
##        for i,card in enumerate(cards):
##            pos = randrange(i,n)
##            cards[i] = cards[pos]
##            cards[pos] = card

    #------------------------------------------------------------

    def AddBottom(self,card):
        

        """ Add a card at the end of the list"""
        
        if self.size < 52:
            return self.cards.append(card)


    #------------------------------------------------------------

    def AddTop(self,card):
        """ Add a card at the top of the deck"""

        if self.size <= 51:
            return self.cards.extend(card)


    #------------------------------------------------------------

    def AddRondom(self,card):
        """Add a card somewhere within the deck"""

        if self.size < 52:
            return self.cards.insert(0,card)
        
        

        
        
