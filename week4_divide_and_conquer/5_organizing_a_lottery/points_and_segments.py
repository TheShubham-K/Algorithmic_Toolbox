# Uses python3
import sys
import random

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    #starts = MergeSort(starts)
    #ends = MergeSort(ends)
    starts = sorted(starts)
    ends = sorted(ends)
#    print(starts, ends)
    for i in range(len(points)):
        st = BinarySearch(starts, points[i], 1)
        end = BinarySearch(ends, points[i], 0)
        #print(st, end)
        cnt[i] = st - end
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

def BinarySearch(a, x, direction): #with direction = 1, work for the 'starts' and 0 for the 'ends'
    if len(a) == 0:
        return -1
    left, right = 0, len(a)-1
    while left <= right:
 #       print(left, right, x, a)
        ave = (left + right) // 2
        if x == a[ave]:
            while left - 1 < ave <= right:
                if x == a[ave]:
                    if direction:  ave += 1
                    else: ave -= 1
                else:break
            if direction: return ave
            else: return ave + 1
        elif x < a[ave]:
            right = ave - 1
        else:
            left = ave + 1
    return right + 1

def MergeSort(a):
    left, right = 0, len(a)
    if right - left <= 1:
        return a
    ave = (left + right) // 2
    sl = MergeSort(a[left:ave])
    sr = MergeSort(a[ave:right])
    return Merge(sl, sr)
def Merge(a, b):
    i, j = 0, 0
    c = []
    while i < len(a):
        if j == len(b):
            c += a[i:]
            break
        if a[i] == b[j]:
            c += 2*[a[i]]
            i += 1
            j += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    if j < len(b):
        c += b[j:]
    return c

if __name__ == '__main__':
    '''
    ###for test
    num = 1000
    Flag = 1
    while Flag:
        s = random.randint(1, num)
        p = random.randint(1, num)
        starts = []
        ends = []
        points = []
        for i in range(s):
            start = random.randint(-num, num)
            dis = random.randint(1, num)
            starts.append(start)
            ends.append(start+dis)
        for j in range(p):
            point = random.randint(-num, num)
            points.append(point)
        cnt_naive = naive_count_segments(starts, ends, points)
        cnt_fast = fast_count_segments(starts, ends, points)
        cnt = 0
        for cnt in range(p):
            if cnt_fast[cnt] != cnt_naive[cnt]:
                print(starts, ends, points)
                print(cnt_naive, cnt_fast)
                Flag = 0
                break
        print("ok")
    ### test
    '''
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
