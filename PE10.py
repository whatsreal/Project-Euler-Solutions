from math import sqrt
#Only need to check against primes below this prime.
#If not divisible by them it is prime.
def isPrime(numToCheck, listPrimes):
    i = 0
    while listPrimes[i] < int(sqrt(numToCheck)+1):
        if numToCheck % listPrimes[i] == 0:
            return False
        i += 1

    return True #Only true if all the primes are checked.


x, y = 5, 0
myPrimes = [3]
while x < 2000000:
    if isPrime(x, myPrimes):
        myPrimes.append(x)
        y += x
        #print y, x
    x += 2


print y + 2+ 3
