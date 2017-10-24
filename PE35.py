from math import sqrt


def isPrime(numToCheck, listPrimes):
    for i in range(0, len(listPrimes)-1):
        if numToCheck % listPrimes[i] == 0:
            return False
    return True #Only true if all the primes are checked.


def isCircular(num, listP):
    numList = []
    while num not in numList:
        numList.append(num)
        tempstr = str(num)
        tempstr = tempstr[1:] + tempstr[0]
        num = int(tempstr)

        if not isPrime(num, listP):
            return 0

    return numList

myList = []
myPrimes = [2]
for i in range(3, 1000000, 2):
    if isPrime(i, myPrimes):
        myPrimes.append(i)
        tempn = isCircular(i, myPrimes)
        if tempn != 0:
            for i in tempn:
                myList.append(i)
print myPrimes
print myList
print len(myList)
