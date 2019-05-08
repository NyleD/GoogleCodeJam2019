

import fileinput


# num is a string
def findAB(num):
    b = ""
    for s in num:
        if s != '\n':
            if s == '4': 
                b += '1'
            else: 
                b += '0'
    numInt = int(num)
    bInt = int(b)
    aInt = numInt - bInt
    return {'A' : aInt, 'B' : bInt}

case = 0
for line in fileinput.input():
    if not (fileinput.isfirstline()):
        case = case + 1
        line.strip()
        AB = findAB(line)
        print("Case #" + str(case) + ": " + str(AB['A']) + " " + str(AB['B']))



