counter = 0 #Counter to find 10 001 prime.
currNum = 3 #current Prime
pastPrimes = [3] #List of smaller primes.


#Only need to check against primes below this prime.
#If not divisible by them it is prime.
def isPrime(numToCheck, listPrimes):
    for i in range(1, len(listPrimes)-1):
        if numToCheck % listPrimes[i] == 0:
            return False
    return True #Only true if all the primes are checked.

while counter < 10000:
    if isPrime(currNum, pastPrimes):
        counter += 1
        pastPrimes.append(currNum)
        #print "The next prime is ", currNum
    currNum += 2

print pastPrimes[len(pastPrimes)-100:]
