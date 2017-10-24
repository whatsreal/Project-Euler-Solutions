sum = 0

for i in range(2, 355000):
    x, y = i, 0
    while (x > 0 and y <= i):
        y += (x%10)**5
        x /= 10

    if i == y:
        sum += i
        print i, sum

print sum
