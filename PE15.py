arr = []
arrSize = 21



for i in range(arrSize):
    temp = []
    for j in range(arrSize):
        if i == 0 or j == 0:
            temp.append(1)
        else:
            temp.append(temp[len(temp) - 1] + arr[i-1][j])
    arr.append(temp)

for i in arr:
    print i
