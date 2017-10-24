def numDigits(x):
    y = 0
    while x > 0:
        y += 1
        x /= 10
        #print x, y
    return y

def fibonacci(curr, prev, counter):
    while numDigits(curr) < 1000:
        temp = prev
        prev = curr
        curr = prev + temp
        counter += 1
    return curr, counter
print fibonacci(1,1,2)
