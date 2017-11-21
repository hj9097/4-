from math import factorial as fact
romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100:'C', 90:'XC',
                  50:'L', 40:'XL',10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

def factorial(numStr):
    try:
        numStr = str(eval(numStr))
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        numStr = str(eval(numStr))
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        numStr = str(eval(numStr))
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        numStr = str(eval(numStr))
        n = int(numStr)
        r = ""
        for value in romans.keys():
            while n >= value:
                r += romans[value]
                n -= value
    except:
        r = "Error!"
    return r

def romanToDec(numStr):
    r = 0
    for i in range (len(numStr)):
        if numStr[i]=='M':
            r += 1000
            continue
        elif numStr[i:i+2] == 'CM':
            r += 900
            i += 1
            continue
        elif numStr[i] == 'D':
            r += 500
            continue
        elif numStr[i:i+2] == 'CD':
            r += 400
            i += 1
            continue
        elif numStr[i] == 'C':
            r += 100
            continue
        elif numStr[i:i+2] == 'XC':
            r += 90
            i += 1
            continue
        elif numStr[i] == 'L':
            r += 50
            continue
        elif numStr[i:i+2] == 'XL':
            r += 40
            i +=1
            continue
        elif numStr[i] == 'X':
            r += 10
            continue
        elif numStr[i:i+2] == 'IX':
            r += 9
            i += 1
            continue
        elif numStr[i] == 'V':
            r += 5
            continue
        elif numStr[i:i+2] == 'IV':
            r += 4
            i += 1
            continue
        elif numStr[i] == 'I':
            r += 1
            continue
        elif numStr[i] not in romans:
            r = 'Error'
            break
    r = str(r)
    return r


def plus(num, numStr):
    if num == 0:
        return factorial(numStr)
    elif num == 1:
        return decToBin(numStr)
    elif num == 2:
        return binToDec(numStr)
    elif num == 3:
        return decToRoman(numStr)
    elif num == 4:
        return romanToDec(numStr)
