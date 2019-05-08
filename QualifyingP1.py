

import fileinput


# num is a string
def findAB(num):
    b = ""
    for s in num:
        if s == '4': 
            b += '1'
        else: 
            b += '0'
    numInt = int(num)
    bInt = int(b)
    aInt = numInt - bInt
    return {'A' : aInt, 'B' : bInt}


for line in fileinput.input():
    line.rstrip()
    case = 0
    if not (fileinput.isfirstline()):
        case += 1
        AB = findAB(line)
        print("#" + case + ": " + AB['A'] + " " + AB['B'])



