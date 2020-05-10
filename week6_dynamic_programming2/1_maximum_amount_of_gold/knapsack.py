# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    value = [[0 for col in range(W + 1)] for row in range(n + 1)]
    for i in range(1, n + 1):
        for cp in range(1, W + 1):
            value[i][cp] = value[i-1][cp]
            if w[i-1] <= cp:
                val = value[i-1][cp - w[i-1]] + w[i - 1]
                if val > value[i][cp]:
                    value[i][cp] = val
#    print(value)
    return value[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
