class LenError(Exception):
    pass

def loadFile(filename):
    """Loads a file that contains numbers in a 20x20 grid.
       Loads those numbers as ints into a 20x20 array.
       Returns that array."""

    finalArray = []
    with open(filename) as f:
        for line in f:
            splitLine = line.split()
            temp = []
            for j in splitLine:
                temp.append(int(j))
            finalArray.append(temp)
        return finalArray


def horizontal(x, y, array):
    """Array is a 20x20 array.  x is the starting location.
       Find the multiplication of 4 consecutive numbers
       on the same line.
       We do the check in here to make sure that there are
       four numbers to add up."""
    if len(array[y]) - x < 4:
        raise LenError("There are not enough ints in that direction")

    val = 1
    for i in range(4):
        val *= array[y][x+i]
    print val
    return val

def vertical(x, y, array):
    if y > 15:
        raise LenError("There are not enough ints in that direction")

    val = 1
    for i in range(4):
        val *= array[y+i][x]
    print val
    return val


def lDiag(x, y, array):
    """Diagonals up towards left."""
    if len(array[y]) - x < 4 or y < 4:
        raise LenError("There are not enough ints in that direction")

    val = 1
    for i in range(4):
        val *= array[y-i][x-i]
    print val
    return val


def rDiag(x, y, array):
    """Diagonals up and to the right"""
    if len(array[y]) - x < 4 or y < 4:
        raise LenError("There are not enough ints in that direction")

    val = 1
    for i in range(4):
        val *= array[y-i][x+i]
    print val
    return val


myArray = loadFile("PE11.hlp")
myTot = 0
for i in range(20):
    for j in range(20):
        for k in range(4):
            try:
                if k == 0:
                    temp = horizontal(i, j, myArray)
                elif k == 1:
                    temp = vertical(i, j, myArray)
                elif k == 2:
                    temp = lDiag(i, j, myArray)
                else:
                    temp = rDiag(i, j, myArray)

                if temp > myTot:
                    myTot = temp
            except LenError:
                pass


print myTot
