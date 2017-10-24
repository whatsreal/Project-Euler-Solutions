def loadFile(filename):
    """Loads a file of filename from same dir.
       each line is one large number.
       Converts to double, returns array of doubles."""
    x = []
    with open(filename) as f:
        for line in f:
            x.append(long(line))

    return x


myArray = loadFile("PE13.hlp")
x = 0
for i in myArray:
    x += i


print x
print str(x)[:10]
