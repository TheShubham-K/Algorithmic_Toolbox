# Uses python3
def edit_distance(s, t):
    #write your code here
    distance = [[0 for col in range(len(s) + 1)] for row in range(len(t) + 1)]
    #print(distance)
    for i in range(len(s) + 1):
        distance[0][i] = i
    for i in range(len(t) + 1):
        distance[i][0] = i
    for m in range(1, len(s) + 1):
        for n in range(1, len(t) + 1):
            ins = distance[n][m-1] + 1
            de = distance[n-1][m] + 1
            mat = distance[n-1][m-1]
            mis = distance[n-1][m-1] + 1
            if s[m-1] == t[n-1]:
                distance[n][m] = min(ins, de, mat)
            else:
                distance[n][m] = min(ins, de, mis)
    return distance[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
