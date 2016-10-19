"""

    pseudo code
PERFECT_SQAURE_FINDEER (num)
    i<- 0
    while i*i< num
       i<- i+1
    if i*i > num
       i<- i-1

    retun i
"""


number = int(input("Enter number: " ))


def perfectSqaureFinder (number):
    i = 0
    while (i*i)< number:
        i+=1
    if (i*i) > number:
        i-=1    
    return i


print(perfectSqaureFinder(number))
        
