from Deck import *
from random import shuffle
from Card import *


class SolitaireGame(object):
    """ a simple Solitaire Game: N cards are dealt face up on the table.
    If two cards have a matching rank, new cards are dealt face up on top of them.
    Dealing continues until the deck is empty, or no two stacks have matching ranks.
    The player wins if all the cards are dealt."""

    def __init__(self, N):
        """Constructor
        pre: N is an integer, denotes the number of piles, s.t. 1 < N < 50
        post: self.size is the number of piles"""

        if N < 1 or N>50:
            raise ValueError
        self.size = N

        
    def newGame(self):
        """ Creates a new game
        post: creates an instance of Solitaire game with N empty places"""
        
        self.deck = Deck() # creating a deck of cards
        self.deck.shuffle() # shuffling them in place
        self.places = [self.deck.deal() for i in range(self.size)] # creating self.size(N) piles, with one card in each
        
        
    def playRound(self):
        """ a round of a game
        pre: all piles are not empty
        post: piles with same rank get new cards on top of them,
        returns True if successful, and False if no cards were placed into piles"""

        
            for j in Card.RANKS:
                if i == j:
                    return False 
                
        
                    
            
                
            
        #find two piles (in self.places) with the cards with the same rank,
        #   say at position i and j
        #deal new cards from the deck into piles i and j
        #return True

        #if piles with cards of the same rank were found, then return False

       
    def playGame(self):
        """ plays a Solitaire game
        post: returns True, if player wins, and False otherwise"""

        roundResult = True # initially, to enter the while loop's body
        
        while roundResult:
            roundResult = playRound()

        if roundResult == True: # all cards were dealt from the deck, success!
            return True
        else: # not all cards were dealt from the deck, the player lost
            return False

              

    def __str__(self):
        """ prints out the layout of top cards at the moment, in self.size(N) piles"""
        

#Tests
# just one presented
s = SolitaireGame(10)
result = s.playGame()
if result == True:
    print("The player won!")
else:
    print("The player lost.")
