# Uses python3
import sys
import random

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m

def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1
    count = -1
    for i in range(n-1):
        previous, current = current, (previous + current) % m
        if current == 1 and previous == 0:
            count = i + 1
            break

    if count < 0:
        return current
    else:
        if n % count <= 1:
            return n % count
        p = 0
        c = 1
        for _ in range(n % count - 1):
            p, c = c, (p + c) % m
        return c

if __name__ == '__main__':
    '''
    while True:
        n = random.randint(1, 1000)
        m = random.randint(2, 1000)
        print ("n: %d, m: %d" % (n, m))
        r1 = get_fibonacci_huge_naive(n, m)
        r2 = get_fibonacci_huge_fast(n, m)
        if r1 == r2:
            print ("ok")
        else:
            print(get_fibonacci_huge_naive(n, m))
            print(get_fibonacci_huge_fast(n, m))
            break
    '''
    input = sys.stdin.read();
    n, m = map(int, input.split())
    #n = 239
    #m = 1000
    #print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))