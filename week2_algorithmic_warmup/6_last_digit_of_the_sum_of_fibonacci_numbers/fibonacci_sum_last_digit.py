# Uses python3
import sys
import random
import time
#import numpy as np
'''
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10
def fib(n):
    if n <= 1:
        return n
    pre = 0
    cur = 1
    for _ in range(n - 1):
        pre, cur = cur, pre + cur
    return cur%10

def fibonacci_sum_fast(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n + 1):
        previous, current = current ,  (previous + current)% 10
    if current > 0:
        return current - 1
    else:
        return 9
def fibsum(n):
    a = np.array([[1, 1], [1, 0]])
    te = np.linalg.matrix_power(a, n+1)
    fn = te[0][0]
    if fn % 10 < 1:
        return 9
    else:
        return fn % 10 -1
def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n // 2)
        c = a * ( b * 2 -a)
        d = a*a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return(d, c+d)
'''
def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1
    count = -1
    i = 0
    while i < n -1:
        previous, current = current, (previous + current) % m
        if current == 1 and previous == 0:
            count = i + 1
            break
        i += 1

    if count < 0:
        return current
    else:
        if n % count <= 1:
            return n % count
        p = 0
        c = 1
        j = 0
        while j < (n % count -1):
            p, c = c, (p + c) % m
            j += 1
        return c

if __name__ == '__main__':
    #n = 832564823476
    '''
    while True:
        n = random.randint(0, 1000)
        #n += 1
        print (n)
        r1 = fibonacci_sum_naive(n)
        #r2 = fibonacci_sum_fast(n)
        r2 = get_fibonacci_huge_fast(n+2, 10)
        if r2 < 1:
            r2 = 9
        else:
            r2 -= 1
        if r1 == r2:
            print ("ok")
        else:
            print(r1)
            print(r2)
            break
        '''
    input = sys.stdin.read()
    n = int(input)
    #t1 = time.time()
    #re = fibonacci_sum_fast(n)
    re =  get_fibonacci_huge_fast(n+2, 10)
    if re < 1:
        re = 9
    else: re -= 1
    print(re)
