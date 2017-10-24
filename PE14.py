largest = 0
x = 0 #longest chain.
for i in range(1, 1000000):
    y = i
    temp = 0
    while y != 1:
        if y % 2 == 0:
            y = y//2
        else:
            y = y * 3 + 1
        temp += 1
    if temp > x:
        x = temp
        largest = i

print largest
