from sys import exit
from math import sqrt

def findDivisors(x):
    a = []
    for i in range(1, int(sqrt(x))+1):
        if x % i == 0:
            a.append(i)
            a.append(x/i)
    return len(a)

x = 1 #current triangle number
y = 0 #num divisors
z = 1 #counter

while True:
    z += 1
    x += z
    y = findDivisors(x)
    if y >= 500:
        print x
        exit()
