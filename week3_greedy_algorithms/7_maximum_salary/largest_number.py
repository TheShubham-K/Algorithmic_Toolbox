#Uses python3

import sys

def isGreatOrEqual(a, b):
    if a + b > b + a:
        return True
    else:
        return False
def largest_number(a):
    #write your code here
    res = ""
    while len(a) > 0:
        maxDigit = '0'
        for x in a:
            if isGreatOrEqual(x, maxDigit):
                maxDigit = x
        res += maxDigit
        a.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
