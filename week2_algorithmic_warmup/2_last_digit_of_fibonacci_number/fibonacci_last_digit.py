# Uses python3
import sys
import random

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10,  previous % 10 + current % 10
    return current % 10
if __name__ == '__main__':
    '''
    while True:
        n = random.randint(0, 10000)
        print (n)
        r1 = get_fibonacci_last_digit_naive(n)
        r2 = get_fibonacci_last_digit_fast(n)
        if r1 == r2:
            print ("ok")
        else:
            print(get_fibonacci_last_digit_fast(n))
            print(get_fibonacci_last_digit_naive(n))
            break
    '''
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_fast(n))
