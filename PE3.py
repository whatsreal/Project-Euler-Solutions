from sys import exit
from math import sqrt
def isPrime(x):
    """Checks to see if x is prime.
       Returns True if it is prime,
       False otherwise."""
    check = 3

    while (check < x/2):
        if (x%check == 0):
            return False
        check += 2

    return True


def findFactor(low, high, number):
    """Find the first factor between low and high for number"""
    #print "In findFactor"
    #print "low = %d, high = %d, number = %d" % (low, high, number)
    #raw_input()
    for i in range(low, high):
        #print "i = %d, i/number = %d, i mod number = %d" % (i, number/i, number%i)
        if number%i == 0 and isPrime(i):
            return i

    return 0


myNum = 600851475143

low, high, biggestPrime = 3, int(sqrt(myNum)), 1
while biggestPrime < high:
    print low, high, biggestPrime, myNum
    temp = findFactor(low, high, myNum)

    if temp > biggestPrime:
        biggestPrime = temp
        low = temp + 2
    else:
        print biggestPrime
        exit(0)
    print "High = %d, Current Biggest Prime = %d, Temp = %d" % (high, biggestPrime, temp)
