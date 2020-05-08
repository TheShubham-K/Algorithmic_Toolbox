# Uses python3
import sys
'''
import random

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current
    if from_ == 0:
        from_ = 1
    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_partial_sum_fast(from_, to):
    if to <= 1:
        return to
    before = 0
    previous = 0
    current = 1

    for _ in range(from_):
        previous, current = current % 10, (previous + current) % 10
    before = current % 10
    for i in range(from_, to + 1):
        previous, current = current % 10, (previous + current) % 10
    if current < before:
        return current - before + 10
    else: return current - before
'''
def get_fibonacci_huge_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    count = -1
    i = 0
    while i < n -1:
        previous, current = current, (previous + current) % 10
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
            p, c = c, (p + c) % 10
            j += 1
        return c



if __name__ == '__main__':
    '''
    while True:
        n = random.randint(0, 10000)
        m = random.randint(0, 10000) + n
        print ("n: %d, m: %d" % (n, m))
        r1 = fibonacci_partial_sum_naive(n, m)
        #r2 = fibonacci_partial_sum_fast(n, m)
        t1 = get_fibonacci_huge_fast(n+1)
        t2 = get_fibonacci_huge_fast(m+2)
        if t2 < t1:
            r2 = 10 + t2 - t1
        else: r2 = t2 - t1
        if r1 == r2:
            print ("ok")
        else:
            print(r1)
            print(r2)
            break
    '''
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    #from_ = 0
    #to = 2
    #print(fibonacci_partial_sum_naive(from_, to))
    t1 = get_fibonacci_huge_fast(from_+1)
    t2 = get_fibonacci_huge_fast(to+2)
    if t2 < t1:
        r2 = 10 + t2 - t1
    else: r2 = t2 - t1

    print(r2)