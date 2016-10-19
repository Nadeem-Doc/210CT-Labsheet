import random

No1 = int(input ("First Number: "))
No2 = int(input ("Second Number: "))
No3 = int(input ("Third Number: "))
No4 = int(input ("Forth Number: "))
No5 = int(input ("Fifth Number: "))

listOfInput = [No1,No2,No3,No4,No5]
"""
ListShuffler takes listOfInput and uses is the lenght of the list as a range
then genereates two random numbers which are used to randomly swap two elements in the list
returns the random list
"""
def ListShuffler(listOfInput):
    for number in range(len(listOfInput)):
        randomNumber1 = random.randrange(0,4)
        randomNumber2 = random.randrange(0,4)
        listOfInput[randomNumber1], listOfInput[randomNumber2] = listOfInput[randomNumber2], listOfInput[randomNumber1]
    return listOfInput


print(ListShuffler(listOfInput))
