"""
‘prime’ is the number to be checked and ‘n’ are where the numbers below are stored
recursively goes through the numbers below ‘prime’. if the base case is reached
then the number is a prime. if at any stage the prime number to be checked is
divisible by ‘n’ then 'prime' isn’t a prime number.
"""

def _primeCheck (prime, n):
    if n == 1:
        return True
    elif prime%n == 0:
        return False
    else:
        return _primeCheck(prime, n-1)

def primeCheck( prime ): #initialises the parameters for  _primeCheck 
    return _primeCheck( prime, prime -1 )# what is the _ used for?

prime = 21
#prime is set to takeaway 1 to that the elif statment isnt triggered 
print( primeCheck(prime))
