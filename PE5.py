def divisibleby(upperBound, numToCheck):
    for i in range(3, upperBound):
        if not numToCheck%i == 0:
            return False
    return True

a = 20
while True:
    if divisibleby(20, a):
        print a
        break
    a += 20
