rows = []
with open('problem-18-data') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])

def searchTriangle(myT):

    if len(myT) < 1:
        print "Not a triangle"
        return
    currTot = 0
    def sTHelp(lNum, p1, p2, myTr):
        if lNum == len(myTr)-1:
            if myTr[lNum][p1] > myTr[lNum][p2]:
                return myTr[lNum][p1]
            else:
                return myTr[lNum][p2]
        else:
            temp1 = sTHelp(lNum + 1, p1, p1+1, myTr) + myTr[lNum][p1]
            temp2 = sTHelp(lNum+1, p2, p2+1, myTr) + myTr[lNum][p2]
            if temp1> temp2:
                return temp1
            else:
                return temp2


    myVar = sTHelp(0,0,0,myT)
    return myVar

print searchTriangle(rows)
