# Uses python3
import sys
import random

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a, b):
    if a < b:
        temp  = a
        a = b
        b = temp
    if b == 0 or b == a:
        return a
    else:
        return gcd_fast(a % b, b)
if __name__ == "__main__":
    '''
    while True:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        print ("a: %d, b: %d" % (a, b))
        gcd1 = gcd_naive(a, b)
        gcd2 = gcd_fast(a, b)
        if gcd1 == gcd2:
            print ("ok")
        else:
            print(gcd1)
            print(gcd2)
            break
    '''
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_fast(a, b))