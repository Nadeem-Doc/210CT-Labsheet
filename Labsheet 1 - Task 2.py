
def trailInFactorial (x):
    count = 0
    for No in range (1,x+1):
        while No> 0:
            if No%5==0:
                No = No/5
                count+= 1
            else:
                break
    return count


userInput = int(input ("Input Number: "))

print(trailInFactorial(userInput))
