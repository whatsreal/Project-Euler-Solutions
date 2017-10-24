rows = []
with open('triangle.txt') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
for x in range(len(rows)-1, 0, -1):
    currRow = rows[x]
    for i in range(0, len(currRow)-1):
        if currRow[i] > currRow[i+1]:
            rows[x-1][i] = rows[x-1][i] + currRow[i]
        else:
            rows[x-1][i] = rows[x-1][i] + currRow[i+1]
#    print rows[x-1]

print rows[0][0]
