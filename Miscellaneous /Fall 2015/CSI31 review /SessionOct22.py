Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> # Oct 22 Class
>>> 
>>> main()
We are going to simulate a game
How many games to simulate? 10
Serving percentage of first player? 0.7
Serving percentage of second player? 0.8
Total number games:  10
Player 1 wins:  3
Player 2 wins:  7
>>> ================================ RESTART ================================
>>> 
>>> main()
We are going to simulate a game
How many games to simulate? 10
Serving percentage of first player? 0.7
Serving percentage of second player? 0.8
Total number games:  10
Player 1 wins:  4
   with percent: 40.0
Player 2 wins:  6
   with percent: 60.0
>>> ================================ RESTART ================================
>>> 
>>> main()
We are going to simulate a series of raquetball games. You will now be asked for some info.
How many games to simulate? 10
Serving percentage of first player? 0.7
Serving percentage of second player? 0.8
Total number games:  10
Player 1 wins:  2
   with percent: 20.0
Player 2 wins:  8
   with percent: 80.0
>>> # Unit Testing
>>> # Unit Testing
>>> GameNotOver(9,14)
True
>>> GameNotOver(9,15)
False
>>> GameNotOver(15,14)
False
>>> GameNotOver(15,15)
False
>>> GameNotOver(15,-14)
False
>>> simOneGame(0.7, 0.8)
(15, 7)
>>> simOneGame(0.11, 0.898)
(0, 15)
>>> simOneGame(0, 0.898)
(0, 15)
>>> simOneGame(0.22, 0.79)
(0, 15)
>>> ================================ RESTART ================================
>>> 
>>> simOneGame(0.11, 0.898)
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
(0, 15)
>>> simOneGame(0.11, 0.898)
A won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
(1, 15)
>>> simOneGame(0.11, 0.898)
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
(0, 15)
>>> simOneGame(0.11, 0.898)
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
(0, 15)
>>> simOneGame(0.11, 0.898)
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
(0, 15)
>>> simOneGame(0.11, 0.898)
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
(0, 15)
>>> simOneGame(0.11, 0.898)
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
(0, 15)
>>> simOneGame(0.11, 0.898)
A won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
B won
A won
B won
A won
B won
(3, 15)
>>> ================================ RESTART ================================
>>> 
>>> simOneGame(0.11, 0.898)
(2, 15)
>>> main()
We are going to simulate a series of raquetball games. You will now be asked for some info.
How many games to simulate? 100
Serving percentage of first player? 0.6
Serving percentage of second player? 0.65
Total number games:  100
Player 1 wins:  32
   with percent: 32.0
Player 2 wins:  68
   with percent: 68.0
>>> main()
We are going to simulate a series of raquetball games. You will now be asked for some info.
How many games to simulate? 100
Serving percentage of first player? 0.6
Serving percentage of second player? 0.62
Total number games:  100
Player 1 wins:  46
   with percent: 46.0
Player 2 wins:  54
   with percent: 54.0
>>> main()
We are going to simulate a series of raquetball games. You will now be asked for some info.
How many games to simulate? 100
Serving percentage of first player? 0.9
Serving percentage of second player? 0.95
Total number games:  100
Player 1 wins:  47
   with percent: 47.0
Player 2 wins:  53
   with percent: 53.0
>>> main()
We are going to simulate a series of raquetball games. You will now be asked for some info.
How many games to simulate? 100
Serving percentage of first player? 0.4
Serving percentage of second player? 0.9
Total number games:  100
Player 1 wins:  0
   with percent: 0.0
Player 2 wins:  100
   with percent: 100.0
>>> main()
We are going to simulate a series of raquetball games. You will now be asked for some info.
How many games to simulate? 0.04
Serving percentage of first player? 0.09
Serving percentage of second player? 4
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    main()
  File "C:\Users\Administrator\Documents\KerryDocs\RaquetBall.py", line 7, in main
    winsA, winsB = simNGames(n,probA,probB)
  File "C:\Users\Administrator\Documents\KerryDocs\RaquetBall.py", line 35, in simNGames
    for i in range(n):
TypeError: 'float' object cannot be interpreted as an integer
>>> main()
We are going to simulate a series of raquetball games. You will now be asked for some info.
How many games to simulate? 100
Serving percentage of first player? 0.04
Serving percentage of second player? 0.09
Total number games:  100
Player 1 wins:  5
   with percent: 5.0
Player 2 wins:  95
   with percent: 95.0
>>> main()
We are going to simulate a series of raquetball games. You will now be asked for some info.
How many games to simulate? 250
Serving percentage of first player? 0.04
Serving percentage of second player? 0.09
Total number games:  250
Player 1 wins:  2
   with percent: 0.8
Player 2 wins:  248
   with percent: 99.2
>>> main()
We are going to simulate a series of raquetball games. You will now be asked for some info.
How many games to simulate? 400
Serving percentage of first player? 0.04
Serving percentage of second player? 0.05
Total number games:  400
Player 1 wins:  108
   with percent: 27.0
Player 2 wins:  292
   with percent: 73.0
>>> 
