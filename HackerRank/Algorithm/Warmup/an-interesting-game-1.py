# -*- coding: utf-8 -*-
"""

Created on Mon Oct 16 13:24:59 2017
https://www.hackerrank.com/challenges/an-interesting-game-1

"""
from operator import itemgetter

#accept the numbe of games
g = int(input().strip())

#loop for the number of games
for a in range(g):
    #number of items in this game
    n = int(input().strip())
    gameValues = []
    position = 0
    for x in input().split():
        #store each item with the value and the position
        entry = [int(x),position]
        gameValues.append(entry)
        position += 1
    
    #sort the values in the descending order based on the value
    sortValues = sorted(gameValues, key = itemgetter(0), reverse = True)
    
    #after it is sorted we loop through the sorted values.
    #we remove one, then find the next highest value with a lower position
    #whenever we find such a value, we increment the number of games.                                                             
    noOfGames = 0
    currentIndexLimit = n
    for item in sortValues:
        if(item[1]<currentIndexLimit):
            noOfGames += 1
            currentIndexLimit = item[1]
    
    if(noOfGames % 2 == 0 ):
        print('ANDY')
    else:
        print('BOB')