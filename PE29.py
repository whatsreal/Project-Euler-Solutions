myList = []

for i in range(2, 101):
    for j in range(2, 101):
        temp = i ** j
        if temp not in myList:
            myList.append(temp)

print len(myList)
