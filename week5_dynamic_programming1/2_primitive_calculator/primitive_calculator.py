# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    '''
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    '''
    optimalnum = DPoptimal(n)
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and optimalnum[n-1] == optimalnum[n // 3 -1] + 1:
            n = n // 3
        elif n % 2 == 0 and optimalnum[n-1] == optimalnum[n // 2 -1] + 1:
            n = n // 2
        else:
            n -= 1
    return reversed(sequence)

def DPoptimal(n):
    optimalnum =n * [0]
    for i in range(2, n+1):
        n1, n2, n3 = -1, -1, -1
        if i % 3 == 0:
            n3 = optimalnum[i // 3 - 1]
        if i % 2 == 0:
            n2 = optimalnum[i // 2 - 1]
        n1 = optimalnum[i - 1 - 1]
        optimalnum[i - 1] = findmin(n3, n2, n1) + 1
    return optimalnum

def findmin(a, b, c):
    if a == -1:
        return findmin(c + 1, b, c)
    if b == -1:
        return findmin(a, c + 1, c)
    return min(a, b, c)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')