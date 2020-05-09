import sys

def lcs2(a, b):
    #write your code here
    L = [[0 for x in range(len(b) + 1)] for x in range(len(a) + 1)]
    ins = [0]*4
    for i in range(len(a)):
        for j in range(len(b)):
            ins[0] = L[i-1][j]
            ins[1] = L[i][j-1]
            mis    = L[i-1][j-1]
            mat    = L[i-1][j-1] + 1
            if a[i-1] == b[j-1]:
                L[i][j] = max(max(ins), mat)
            else:
                L[i][j] = max(ins)
    return L[i][j]

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

    print(lcs2(a, b))