tens = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
ones = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,
        10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}

hundreds = 0
myCount = 0
for i in range(0, 10):
    prefix = ones[i] + hundreds
    temp = prefix - 3
    for j in range(1, 20):
        temp += ones[j] + prefix -3
        #print i*100+j, ones[j]+prefix
    for j in range(20, 100):
        temp += prefix + tens[j//10] + ones[j%10]
        #print i*100+j, prefix+tens[j//10]+ones[j%10]
    myCount += temp
    hundreds = 10
    print temp, myCount



print myCount+11, "Try1"


##Try Two
#each "hundred" occurs 100 times
#each 1-99 occurs 10 times

myCount2 = 0
for i in range(1, 10):
    myCount2 += (ones[i] + 10) * 100

for j in range(1, 20):
    myCount2 += ones[j] * 10

for k in range(20, 100):
    myCount2 += (tens[k/10] + ones[k%10]) * 10

print myCount2 + 11, "Try 2"


##Try Three
#Just loop from 1-1000
myCount3 = 0
for i in range(1, 1001):
    if i % 10 > 0:
        myCount3 += ones[i%10]
    if i % 100 == 10:
        myCount3 += 3
    elif i % 100 > 10 and i % 100 < 20:
        myCount3 += ones[i%100]
    elif i % 100 >= 20:
        myCount3 += tens[(i%100)//10]

    if i % 1000 > 0:
        myCount3 += ones[(i%1000)//100] + 10

print myCount3 + 11, "Try 3"

##Try 4
total = 0
mhundred = 7
mand = 3
mthousand = 8
mones = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,8,8,8,8]
mtens = [0,0,6,6,5,5,5,7,6,6]
for i in range(1, 1000):
    a = i//100
    b = i//10 - a*10
    c = i%10

    if a != 0:
        total += mones[a] + mhundred
        if b != 0 or c!= 0:
            total += mand

    if b == 0 or b == 1:
        total += mones[b*10 + c]
    else:
        total+= mtens[b] + mones[c]

total += mthousand + 

print total, "Try 4"
