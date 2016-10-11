"""
include real docstrings and correct variable names
"""

import random

x = int(input ("first: "))
y = int(input ("first: "))
t = int(input ("first: "))
f = int(input ("first: "))
d = int(input ("first: "))

listOfInput = [x,y,t,f,d]
for i in range(len(listOfInput)):
    randomNumber1 = random.randrange(0,4)
    randomNumber2 = random.randrange(0,4)
    listOfInput[randomNumber1], listOfInput[randomNumber2] = listOfInput[randomNumber2], listOfInput[randomNumber1]

print(listOfInput)




