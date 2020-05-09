# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    #print(number_of_inversions)
    b = a
    sorteda, numOfInve = Merge(b[left: ave], b[ave: right])
    #print(sorteda, numOfInve)
    b[left:right] = sorteda
    number_of_inversions += numOfInve
    #print(b, numOfInve, number_of_inversions)
    return number_of_inversions



def Merge(a, b):
    c = []
    i = 0
    j = 0
    numOfInversions = 0
    while i < len(a):
        if j == len(b):
            c += a[i:]
            #numOfInversions += (len(a) - i - 1) * len(b)
            break
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            numOfInversions += (len(a) - i)
            j += 1
        else:
            c.append(a[i])
            i += 1
    if j < len(b):
        c += b[j:]
    return c, numOfInversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))