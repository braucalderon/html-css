# A "stub" of object-oriented raquetball
# Class keeps track of the statistics for the games played
# In particular, keeps track of the number of wins and number of
# shut-outs for each

playerclass SimStats:
    def __init__(self):
        self.a = 9 # temporary dumb line

        def update(self,game):
            x = 4 # temporary dumb line

        def printReport(self):

            print("Here's the report!")

            # Class used to simulate a single

            gameclass RBallGame:

                def __init__(self,probA,probB):
                    self.probA = probA
                    self.probB = probB

                def play(self):
                    x = 4 # temporary dumb line

                def main():
                    print_intro()
                    probA, probB, n = getInputs()

                    stats = SimStats()

                    for i in range(n):
                        theGame = RBallGame(probA,probB)
                        theGame.play()
                        stats.update(theGame)

                    stats.printReport()

            # Prints an introduction to the user

            def print_intro():
                print("We are going to simulate a series of raquetball games. You will now be asked for some info.")

                # Prompts the user for 3 values:
                #    1- number of games
                #    2- serving percentage of player 1
                #    3- serving percentage of player 2

            def getInputs():
                n = eval(input("How many games to simulate? "))
                probA = eval(input("Serving percentage of first player? "))
                probB = eval(input("Serving percentage of second player? "))
                return probA, probB, n

