import sys, random, time

def lcs2(a, b):
    m =len(a)
    n =len(b)
    #write your code here
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]
    ins = [0]*4
    for i in range(m+1):
        for j in range(n+1):
            if a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]
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
    
    
