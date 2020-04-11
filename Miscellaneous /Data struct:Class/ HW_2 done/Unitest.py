# unitTestingCard.py
# unit testing rank

import sys
import unittest

from Card import *

class RankTest(unittest.TestCase):
  """ Tests Rank methods: rank() and rankName() """
  
  def testRanks(self): # unit test for ranks 1-13
    """ creates cards of rank 1 through 13 of clubs and
    verifies that the created card's rank is equal to the
    rank it was created with """
    
    for i in range(2,15):
      myCard = Card(i,'c') # create i of clubs
      self.assertEqual(myCard.rank(),i) # verifies that the card's rank is i

  def testRankName(self): # unit test for rank names, 'ace', 'two', 'three',...
    """ creates cards with rank names "ace", ...
    and then checks for equivalency: card's rank name, by calling method rankName,
    and the rank name that was given to the card"""

    for t in range(1,14):
      myCard = Card(t,'c')
      #print(myCard)
      self.assertEqual(myCard.rankName(),Card.RANK_NAMES[t-1])


class SuitTest(unittest.TestCase):
  """ Tests Suit methods: suit() and suitName() """
    
  def testSuits(self): # unit test for suits, 'c', 'd', 'h', 's'
    """ creates cards of rank ...  of c (clubs), d (diamonds),
    h(hearts) and s (spades), and verifies that the created card's suit
    is equal to the suit it was created with (c,d,h,s) """

    for i in range(2,14):
        for k in ('c','d','h','s'):
            myCard = Card(i, k)
            #print (myCard)
            self.assertEqual(myCard.suit(), k)
    
  def testSuitName(self): # unit test for suit names, 'clubs', 'diamonds',...
    """ creates cards with all the suit names ...
    and then checks for equivalency: card's suit name, by calling method suitName,
    and the suit name that was given to the card"""

    for i in Card.SUITS:
      myCard = Card(1,i)
      #print (myCard)
      self.assertEqual(myCard.suitName(), Card.SUIT_NAMES[Card.SUITS.index(i)])
      

    
    
def main(argv):
  unittest.main()

if __name__ == '__main__':
  main(sys.argv)



  
