def reverseNum2(x):
    y = 0
    while x  > 0:
        y *= 10
        y += x%10
        x = x/10
        #y = y * 10
    return y

def isPalindrome(x):
    return x == reverseNum2(x)

a = 99
b = 99
current = 0

while a<=999:
    while b<=999:
        if isPalindrome(a*b) and a*b > current:
            print a*b, current
            current = a*b
        b += 1
    b = 99
    a += 1

print current
