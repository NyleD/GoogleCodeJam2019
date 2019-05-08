



def boolPrint(bool):
    if bool:
        return 'POSSIBLE'
    
    return 'IMPOSSIBLE'


def numberCovered(startr, startc, endr, endc):
    covered = 0

    for i in range(startr, endr):
        for k in range(startc, endc):
            if (Grid[i][k]):
                covered += 1
    return covered

def findLine(direction, index):
    
    if direction == 'row':
        return numberCovered(index, 0, index + 1, C)
    if direction == 'col':
        return numberCovered(0, index, R, index + 1)


def countSoFarCol(val):
    for k in range(C):
        if val > findLine('col', k):
            return False
    return True

def countSoFarRow(val):
    for i in range(R):
        if val > findLine('row', i):
            return False
    return True

def completeGrid(Grid):
    for i in range(R):
        for k in range(C):
            if Grid[i][k] != 1:
                return False 
    return True

def printPoints(Points):
    for l in Points: 
            print(str(l[0]) + " " + str(l[1]))

def validCell(r, c, nr, nc):
    if r == nr or c == nc or (r - c) == (nr - nc) or (r + c) == (nr + nc):
        return False
    return True

def findAnswer(Grid):
    Grid[0][0] = 1

    r = 0
    c = 0
    rowCount = 1
    colCount = 1

    while not (completeGrid(Grid)):
        
        if countSoFarRow(rowCount):
            rowCount = rowCount + 1
        
        if countSoFarCol(colCount):
            colCount = colCount + 1

        found = False
        for nr in range(R):
            for nc in range(C):
                if (not Grid[nr][nc]) and validCell(r,c, nr, nc): #  Valid
                    if (findLine('row', nr) < rowCount) and (findLine('col', nc) < colCount):
                        point = [nr+1,nc+1]
                        Points.append(point)
                        found = True
                        Grid[nr][nc] = 1
                        r = nr
                        c = nc
                        break
            if found:
                break

        if not found:
            return False
    
    return True
    


# INPUT / OUTPUT
test_cases = int(input())

for i in range(1, test_cases + 1):
   
    # Global Varaibles
    dimensions = input()
    R = int(dimensions[0])
    C = int(dimensions[2])
    Grid = [[0 for x in range(C)] for y in range(R)]
    Points = [[1,1]]

    val = findAnswer(Grid)
    out =  boolPrint(val)
    print("Case #" + str(i) + ": " + out)
    if val:
        printPoints(Points)


