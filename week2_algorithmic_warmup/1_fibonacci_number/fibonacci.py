# Uses python3
import random

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fib(n):
    if (n <= 1):
        return n
    f0 = 0
    f1 = 1
    i = 2
    while i <= n:
        f = f0 + f1
        f0 = f1
        f1 = f
        i += 1
    return f

n = int(input())
print(fib(n))
'''
if __name__ == '__main__':
    while True:
        n = random.randint(0, 10)
        print(n)
        fib1 = calc_fib(n)
        fib2 = fib(n)
        if fib1 != fib2:
            print(calc_fib(n))
            print(fib(n))
            break
        else:
            print ("ok")
'''