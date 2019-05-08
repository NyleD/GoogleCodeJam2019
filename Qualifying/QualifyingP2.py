





def endOfGrid(dim, firstMove, path):
    
    east = 1
    south = 1

    firstColNoSouth = 1
    firstRowNoEast = 1

    path = path[:-1]

    for c in path:
        if c == 'E':
            if south == firstRowNoEast:
                firstRowNoEast += 1
            east += 1
        if c == 'S':
            if east == firstColNoSouth:
                firstColNoSouth += 1
            south += 1
    
    if firstMove == 'E' and (east == dim):
        return firstColNoSouth
    elif firstMove == 'S' and (south == dim):
        return  firstRowNoEast
        
    return -1
    

def getOpposite(firstMove):
    if firstMove == 'S':
        return 'E'
    else:
        return 'S'


def findPath(dim, path):
    myPath = ""
    cutPath = 0

    if path[0] == 'S':
        myPath += 'E'
        cutPath = endOfGrid(dim, 'E', path)
    else:  # == 'E'
        myPath += 'S'
        cutPath = endOfGrid(dim, 'S', path)

    firstMove = myPath[0]
    directionOpp = getOpposite(firstMove)

    if cutPath == -1:
        
        for i in range(dim - 2):
            myPath += firstMove
        for i in range(dim - 1):
            myPath += directionOpp

    else:
        for i in range(cutPath - 2):
            myPath += firstMove
        for i in range(dim - 1):
            myPath += directionOpp
        for i in range(dim - cutPath):
            myPath += firstMove

    return myPath  



# INPUT / OUTPUT

test_cases = int(input())

for i in range(1, test_cases + 1):
    # Reading 2 lines at a time (Int, String)
    dimMaze = int(input())
    direction = input()
    out = findPath(dimMaze, direction)
    print("Case #" + str(i) + ": " + out)


