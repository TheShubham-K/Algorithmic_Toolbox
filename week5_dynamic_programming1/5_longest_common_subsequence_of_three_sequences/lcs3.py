#Uses python3

import sys, time, random

def lcs3(a, b, c):
    #write your code here
    lcsmat = [[[0 for x in range(len(a) + 1)] for y in range(len(b) + 1)] for z in range(len(c) + 1)]
    ins = [0]*6
    for z in range(1, len(c) + 1):
        for y in range(1, len(b) + 1):
            for x in range(1, len(a) + 1):
                ins[0] = lcsmat[z][y][x-1]
                ins[1] = lcsmat[z][y-1][x]
                ins[2] = lcsmat[z][y-1][x-1]
                ins[3] = lcsmat[z-1][y][x]
                ins[4] = lcsmat[z-1][y][x-1]
                ins[5] = lcsmat[z-1][y-1][x]
                mis = lcsmat[z-1][y-1][x-1]
                mat = lcsmat[z-1][y-1][x-1] + 1
                if a[x-1] == b[y-1] == c[z-1]:
                    lcsmat[z][y][x] = max(max(ins), mat)
                else:
                    lcsmat[z][y][x] = max(max(ins), mis)

    return lcsmat[-1][-1][-1]
if __name__ == '__main__':
    '''
    ### test
    an = random.randint(30, 100)
    a =[]
    for i in range(an):
        a.append(random.randint(-100, 100))
    bn = random.randint(30, 100)
    b =[]
    for i in range(bn):
        b.append(random.randint(-100, 100))
    cn = random.randint(30, 100)
    c = []
    for i in range(cn):
        c.append(random.randint(-100, 100))
    start = time.time()
    result = lcs3(a, b, c)
    end = time.time()
    print(result)
    print('the running time is %0.5f s' % (end-start))
    ### test
    '''
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
