from math import sqrt

def findSumDivisors(x):
    a = []
    for i in range(1, int(sqrt(x))+1):
        if x % i == 0:
            a.append(i)
            a.append(x/i)
    y = 0
    for i in a:
        y += i
    return y-x


listAN = []
for i in range(1, 10001):
    t1 = findSumDivisors(i)
    t2 = findSumDivisors(t1)
    string = "I am checking " + str(i) + ", " + str(t1) + ", " + str(t2)
    if t2 == i and t1 != i:
        if i not in listAN:
            listAN.append(i)
            string += " appended " + str(i)
        if t1 not in listAN:
            listAN.append(t1)
            string += " appended " + str(t1)
    #print string

print listAN

mySum = 0
for j in listAN:
    mySum += j

print mySum
