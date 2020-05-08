# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    vpw = []
    for w, v, i in zip(weights, values, list(range(n))):
        vpw.append((float(v / w), i)) #using tuple for better good
    vpw = sorted(vpw, key = lambda t: t[0], reverse = True)
    j = 0
    while capacity > 0 and j < n:
        weight = weights[vpw[j][1]]
        if weight > capacity:
            value += capacity * vpw[j][0]
            break
        else:
            value += values[vpw[j][1]]
            capacity -= weight
            j += 1
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))