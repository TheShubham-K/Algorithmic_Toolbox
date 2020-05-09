# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = int((left + right) / 2)
    rlow = get_majority_element(a, left, mid)
    rright = get_majority_element(a, mid, right)
    if rleft == rright and rleft != -1:
        return rleft
    elif rleft != -1 and rright == -1:
        return rleft
    elif rright != -1 and rleft == -1:
        return rright
    else:
        cleft = 0
        cright = 0
        for t in a[left : right]:
            if t == rleft:
                cleft += 1
            if t == rright:
                cright += 1
        if cleft > cright:
            return cleft
        elif cleft < cright:
            return cright
    return -1

def getMajorityElement(a):
    candidate = -1
    count = 0
    for t in a:
        if count == 0:
            candidate, count = t, 1
            continue
        if t == candidate:
            count += 1
        else:
            count -= 1
    recount = 0
    for x in a:
        if x == candidate:
            recount  += 1
    if recount > len(a) // 2:
        return candidate 
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
#     if get_majority_element(a, 0, n) != -1:
#         print(1)
#     else:
#         print(0)
    #print (get_majority_element(a, 0, n))
    #print (getMajorityElement(a))
    if getMajorityElement(a) != -1:
        print(1)
    else:
        print(0)