# Uses python3
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    n = (len(dataset) + 1) // 2
    MAX = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        MAX[i][i] = int(dataset[2*i])
    MIN = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        MIN[i][i] = int(dataset[2*i])
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            MAX[i][j], MIN[i][j] = MinAndMax(i, j, MAX, MIN, dataset)
    return MAX[0][-1]

    return 0
def MinAndMax(i, j, MAX, MIN, dataset):
#    tmin = math.inf #for python 3.5
#    tmax = -math.inf
    tmin = float("inf")
    tmax = -float("inf")
    for k in range(i, j):
        a = evalt(MAX[i][k], MAX[k+1][j], dataset[2*k+1])
        b = evalt(MAX[i][k], MIN[k+1][j], dataset[2*k+1])
        c = evalt(MIN[i][k], MAX[k+1][j], dataset[2*k+1])
        d = evalt(MIN[i][k], MIN[k+1][j], dataset[2*k+1])
        tmin = min(tmin, a, b, c, d)
        tmax = max(tmax, a, b, c, d)
    return tmax, tmin

if __name__ == "__main__":
    print(get_maximum_value(input()))
