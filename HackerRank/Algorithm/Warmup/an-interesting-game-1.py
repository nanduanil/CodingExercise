# -*- coding: utf-8 -*-
"""

Created on Mon Oct 16 13:24:59 2017
https://www.hackerrank.com/challenges/an-interesting-game-1

"""

#accept the numbe of games
g = int(input().strip())

#loop for the number of games
for a in range(g):
    #number of items in this game
    n = int(input().strip())
    maxSoFar = 0
    noOfGames = 0
    for x in input().split():
        currentValue = int(x)
        #as we read the inputs, if current item is larger than the max so far, 
        #we can play one more game
        if(currentValue > maxSoFar):
            noOfGames += 1
            maxSoFar = currentValue
            
    if(noOfGames % 2 == 0 ):
        print('ANDY')
    else:
        print('BOB')
