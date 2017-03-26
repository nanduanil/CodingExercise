# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:37:16 2017
problem : https://www.hackerrank.com/challenges/journey-to-the-moon
@author: nandu
"""
#%%
commandLineString = input()
commandLine = [int(x) for x in commandLineString.split()]

astronauts = []
#get all the inputs
for i in range(0,commandLine[1]):
    inputAstr = [int(x) for x in input().split()] 
    
    astr1_Present = False
    astr2_Present = False
    #find if one of the astronaut already in list
    #if so add the other
    #if both present do nothing
    for c in range(0,len(astronauts)):
        country = astronauts[c]
        for astr in country:
            if(astr == inputAstr[0]):
                astr1_Present = True
                astr1_Country = c
            if(astr == inputAstr[1]):
                astr2_Present = True
                astr2_Country = c
        #if both found stop searching
        if(astr1_Present and astr2_Present):
            break
    #add the new data 
    if(astr1_Present and astr2_Present):
        if(astr1_Country == astr2_Country):
            continue
        else:
            astronauts[astr1_Country] = astronauts[astr1_Country] + astronauts[astr2_Country] 
            astronauts.pop(astr2_Country)
    elif(astr1_Present):
        astronauts[astr1_Country].append(inputAstr[1])
    elif(astr2_Present):
        astronauts[astr2_Country].append(inputAstr[0])
    else:
        astronauts.append(inputAstr)
    
    
TotalCombinations = (commandLine[0] * (commandLine[0] -1))/2
missedCombinations = 0
for country in astronauts:
    numberOfAstr = len(country)
    missedCombinations = missedCombinations + ((numberOfAstr * (numberOfAstr-1))/2)
    
print(int(TotalCombinations - missedCombinations))


                     



