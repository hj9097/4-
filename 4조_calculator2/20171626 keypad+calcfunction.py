# Keypad
numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantList = {
    'pi':'3.141592',
    '빛의 이동 속도 (m/s)':'3E+8',
    '소리의 이동 속도 (m/s)':'340',
    '태양과의 평균 거리 (km)':'1.5E+8',
}

functionList = [
    'factorial (!)',
    '-> binary',
    'binary -> dec',
    '-> roman',
]
##############################################################
# calcfunction
from math import factorial as fact


def func(key, numStr):
    if key == 'factorial (!)':
        try:
            numStr = str(eval(numStr))
            n = int(numStr)
            r = str(fact(n))
        except:
            r = 'Error!'
        return r
    elif key == '-> binary':
        try:
            numStr = str(eval(numStr))
            n = int(numStr)
            r = bin(n)[2:]
        except:
            r = 'Error!'
        return r
    elif key == 'binary -> dec':
        try:
            numStr = str(eval(numStr))
            n = int(numStr, 2)
            r = str(n)
        except:
            r = 'Error!'
        return r
    elif key == '-> roman':
        return 'dec -> Roman'
