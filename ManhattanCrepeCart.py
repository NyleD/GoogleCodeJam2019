


def findMaxGrid(Grid, size):
    x = size + 1
    y = size + 1
    
    maxsofar = 0
    maxinter = []
    for i in range(x):
        for k in range(y):
            if Grid[i][k] > maxsofar:
                maxinter.clear()
                maxsofar = Grid[i][k]
                maxinter.append([i,k])
            elif Grid[i][k] == maxsofar:
                maxinter.append([i,k])

    return str(maxinter[0][0]) + " " + str(maxinter[0][1])                 
# INPUT / OUTPUT

test_cases = int(input())

for i in range(1, test_cases + 1):
    # Reading 2 lines at a time (Int, String)
    details = input()
    splitDetails = details.split()
    people = int(splitDetails[0])
    grid = int(splitDetails[1])

    Grid = [[0 for x in range(grid+1)] for y in range(grid+1)] 
    for k in range(people):
        person = input() 
        splitDirection = person.split()
        x = int(splitDirection[0])
        y = int(splitDirection[1])
        if splitDirection[2] == 'N':
            
            while(y < (grid)):
                y = y + 1
                for x in range(0,grid+1):
                    Grid[x][y] += 1
        if splitDirection[2] == 'S':
            
            while(y > 0):
                y = y - 1
                for x in range(0,grid+1):
                    Grid[x][y] += 1
        if splitDirection[2] == 'E':
            
            while(x < (grid)):
                x = x + 1
                for y in range(0,grid+1):
                    Grid[x][y] += 1
        if splitDirection[2] == 'W':
            
            while(x > 0):
                x = x - 1
                for y in range(0,grid+1):
                    Grid[x][y] += 1


    out = findMaxGrid(Grid, grid)
    print("Case #" + str(i) + ": " + out)


