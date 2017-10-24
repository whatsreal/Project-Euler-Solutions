from sys import exit


def findTriple(x):
    """Accepts a number x.
       Returns two numbers y, z
       where y**2 + z**2 == x**2"""
    y, z = [], []
    for i in range(2,x-1):
        for j in range(i,x-2):
            if (i**2 + j**2 == x**2):
                y.append(i)
                z.append(j)
            elif (i**2 + j**2 > x**2):
                break
    return y, z

a, b, c = 1, 1, 3

while True:
    a, b = findTriple(c)
    #print a, b, c

    if (len(a) > 0):
        for i in range(len(a)-1):
            if (a[i] + b[i] + c == 1000):
                print a[i] * b[i] * c
                print a[i], b[i], c
                exit(0)
            else:
                print a[i], b[i], c, " Did not work..."
    c += 1
