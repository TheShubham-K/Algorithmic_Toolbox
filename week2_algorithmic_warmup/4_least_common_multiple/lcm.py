# Uses python3
import sys
import random

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
def gcd(a, b):
    if a < b:
        t = a
        a = b
        b = t

    if b == 0 or b == a:
        return a
    else:
        return gcd(a % b, b)
def lcm_fast(a, b):
    return a*b // gcd(a, b)
if __name__ == '__main__':
    '''
    while True:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        print ("a: %d, b: %d" % (a, b))
        r1 = lcm_naive(a, b)
        r2 = lcm_fast(a, b)
        if r1 == r2:
            print ("ok")
        else:
            print (r1)
            print (r2)
            break
    '''
    #print(lcm_fast(18, 35))
    #print(lcm_fast(226553150, 1023473145))
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))
    #print('%.f' % (lcm_fast(a, b)))