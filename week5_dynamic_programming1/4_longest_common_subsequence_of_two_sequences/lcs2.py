import sys
import random
import time


def lcs2(m, wt, val, n):
    # write your code here
    L = [[None]*(n + 1) for x in range(m + 1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif val[i-1] == wt[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[n][m]


if __name__ == '__main__':

    n = int(input())
    val = list(map(int, input().split()))
    m = int(input())
    wt = list(map(int, input().split()))
    print(lcs2(m, wt, val, n))
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))

    # n = data[0]
    # data = data[1:]
    # a = data[:n]

    # data = data[n:]
    # m = data[0]
    # data = data[1:]
    # b = data[:m]


#    an = random.randint(0, 100)
#    a =[]
#    for i in range(an):
#        a.append(random.randint(0, 100))
#    bn = random.randint(30, 100)
#    b =[]
#    for i in range(bn):
#        b.append(random.randint(0, 100))
#    start = time.time()
#    print(a)
#    print(b)
#    result = lcs2(a, b)
#    end = time.time()
#    print(result)
#    print('the running time is %0.5f s' % (end-start))
