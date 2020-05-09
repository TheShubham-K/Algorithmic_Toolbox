  
#Uses python3
import sys
import math
import random
#import functools
def mini_naive(n, x, y):
    mini = float("inf")
    for i in range(n):
        j = i + 1
        while j < n:
            d = math.sqrt(power2(x[j]-x[i])+power2(y[j]-y[i]))
            if mini > d: mini = d
            j += 1
    return ("%0.5f" % mini)
def minimum_distance(x, y):
    #write your code here
    assert len(x) == len(y), "Error with the cordinates of the points"
    points = sorted(zip(x, y), key=lambda t:t[0])
    return distance(points)

def distance(x):
    if len(x) == 2:
        return dis(x[0], x[1])
    elif len(x) == 1:
        return -1
    mid = len(x) // 2
    Ldis = distance(x[0:mid])
    Rdis = distance(x[mid:])
    if Ldis * Rdis <= 0: td = abs(Ldis * Rdis) #or return -Ldis * Rdis
    else: td = min(Ldis, Rdis)
    #print(td)
    middle_points = []
    for point in x:
        if abs(point[0]-x[mid][0]) <= td:
            middle_points.append(point)
    middle_points = sorted(middle_points, key = lambda x: x[1])
    return distance_y(td, middle_points)
    '''
    for lpoint in x[0:mid]:
        for rpoint in x[mid:]:
            if rpoint[0] - lpoint[0] > td:
                break
            if abs(rpoint[1] - lpoint[1]) > td:
                continue
            td = min(td, dis(lpoint, rpoint))
    #return ("%0.5f" % td)
    return td
    '''

def distance_y(d, middle_points):
    n = len(middle_points)
    for i in range(n):
        j = i + 1
        while j < n:
            if middle_points[j][1] - middle_points[i][1] > d:
                break
            d = min(d, dis(middle_points[i], middle_points[j]))
            j += 1
    return d

def dis(a, b):
    return math.sqrt(power2(a[0]-b[0]) + power2(a[1]-b[1]))

def power2(x):
    return x*x
if __name__ == '__main__':
    '''
    ### test
    num = 1000
    while True:
        x =[]
        y = []
        n = random.randint(2, num)
        for i in range(n):
            x.append(random.randint(-num, num))
            y.append(random.randint(-num, num))
        re_naive = mini_naive(n, x, y)
        re_temp= minimum_distance(x, y)
        re_fast ="%.5f" % re_temp
        if re_fast == re_naive: print("ok", n)
        else:
            print(x, y)
            print(re_fast, re_naive)
            break
    ###
    '''
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.10f}".format(minimum_distance(x, y)))