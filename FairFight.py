


def findMax(swords, start, end):
    maxsofar = swords[start]
    for i in range(start, end):
        if  swords[i] > maxsofar:
            maxsofar = swords[i]
    return maxsofar   


def toInt(swords):

    i = 0
    for a in swords:
        swords[i] = int(a)
        i += 1
    return swords

# INPUT / OUTPUT

test_cases = int(input())

for i in range(1, test_cases + 1):
    # Reading 2 lines at a time (Int, String)
    details = input()
    splitDetails = details.split()
    swords = int(splitDetails[0])
    maxdifference = int(splitDetails[1])

    A = input() 
    Aswords = A.split()
    B = input()
    Bswords = B.split()
    Aswords = toInt(Aswords)
    Bswords = toInt(Bswords)

    count = 0

    for start in range(swords):
        end = start + 1
        while (end <= swords):
            
            Ascore = findMax(Aswords, start, end)
            Bscore = findMax(Bswords, start, end)
            
            if abs(Ascore-Bscore) <= maxdifference:
                count += 1

            end += 1 

    out = str(count)
    print("Case #" + str(i) + ": " + out)


