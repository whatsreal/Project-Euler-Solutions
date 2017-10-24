f1 = 1
f2 = 2
sum = 0

while f2 < 4000000:
    if f2%2 == 0:
        sum += f2

    temp = f1 + f2
    f1 = f2
    f2 = temp

print sum
