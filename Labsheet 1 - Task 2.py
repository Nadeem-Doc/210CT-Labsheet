"""
Takes the user input as the factorial. when the 'No'
reaches a point where its divisible by five count is incremented.
"""

def trailInFactorial (factorial):
    count = 0
    for No in range (1,factorial+1):
        while No> 0:
            if No%5==0:
                No = No/5 #No will continue where it was left off in fo loop    
                count+= 1
            else:
                break
    return count

userInput = int(input ("Input Number: "))
print(trailInFactorial(userInput))
