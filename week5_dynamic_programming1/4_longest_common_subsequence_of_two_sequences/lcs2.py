# Uses python3

import sys


def lcs2(a, b):
    # write your code here
    result = [[0 for j in range(m+1)] for i in range(n + 1)]
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if a[x - 1] == b[y - 1]:
                result[x][y] = result[x - 1][y - 1] + 1
            else:
                result[x][y] = max(result[x - 1][y], result[x][y - 1])
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    result = lcs2(a, b)
    print(result[n][m])
