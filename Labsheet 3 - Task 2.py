"""
‘prime’ is the number to be checked and ‘n’ are where the numbers below are stored
recursively goes through the numbers below ‘prime’. if the base case is reached
then the number is a prime. if at any stage the prime number to be checked is
divisible by ‘n’ then 'prime' isn’t a prime number.
"""

def primeCheck2 (prime, n):
    if n == 1:
        return True
    elif prime%n == 0:
        return False
    else:
        return primeCheck2(prime, n-1)

def primeCheck( prime ): #initialises the parameters for  _primeCheck 
    return primeCheck2( prime, prime -1 )

prime = 29
#prime is set to takeaway 1 to that the elif statment isnt triggered 
print( primeCheck(prime))
