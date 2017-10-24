x = 100 #upper bound
sumSquares = 0
squareSum = 0
#Sum of the Squares
for i in range(1,x+1):
    sumSquares += (i*i)
    squareSum += i

squareSum = squareSum*squareSum

print squareSum - sumSquares
