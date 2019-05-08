
#### HELPER FUNCTIONS ##########


def boolPrint(bool):
    if bool:
        return 'POSSIBLE'
    
    return 'IMPOSSIBLE'

def numberChipsPiece(startr, startc, endr, endc):
    chips = 0

    for i in range(startr, endr):
        for k in range(startc, endc):
            if (Waffle[i][k]):
                chips += 1
    return chips

def findChipsLine(direction, index):
    
    if direction == 'row':
        return numberChipsPiece(index, 0, index + 1, C)
    if direction == 'col':
        return numberChipsPiece(0, index, R, index + 1)


#### MAIN LOGIC TIES ALL HELPER FUNCTIONS

def findAnswer():

    if H == 0 and V == 0:
        return True

    HCuts = []
    VCuts = []

    totalChips = numberChipsPiece(0, 0, R, C)
    if totalChips % ((H + 1) * (V + 1)):
         return False
    
    chipsEach = totalChips / ((H + 1) * (V + 1))

    if totalChips % (H + 1) or totalChips % (V + 1):
        return False 
    
    chipsH = totalChips / (H + 1)
    chipsV = totalChips / (V + 1)

    sofar = 0
    for i in range(R):
        sofar += findChipsLine('row', i)
        if sofar == chipsH:
           HCuts.append(i + 1)
           sofar = 0
        elif (sofar > chipsH):
            return False
    
    if len(HCuts) <= H:
        return False
    
    sofar = 0
    for i in range(C):
        sofar += findChipsLine('col', i)
        if sofar == chipsV:
           VCuts.append(i + 1)
           sofar = 0
        elif (sofar > chipsV):
            return False
    
    if len(VCuts) <= V:
        return False

    startr = 0
    for endr in HCuts:
        startc = 0
        for endc in VCuts:
            if numberChipsPiece(startr, startc, endr, endc) != chipsEach:
                return False
            startc = endc
        startr = endr
    
    return True

########## INPUT / OUTPUT ########

test_cases = int(input())

# Looping thorugh all test cases 
for t in range(1, test_cases + 1):
    
    # GLOBAL Variables

    dimensions = input()
    R = int(dimensions[0])
    C = int(dimensions[2])
    H = int(dimensions[4])
    V = int(dimensions[6])
    # 2D array
    Waffle = [[0 for x in range(C)] for y in range(R)]

    for i in range(R):
        row = input()
        for k in range(C):
            if row[k] == '@':
                Waffle[i][k] = 1 
    
    # OUTPUT:
    out = boolPrint(findAnswer())
    print("Case #" + str(t) + ": " + out)
