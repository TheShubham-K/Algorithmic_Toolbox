# Uses python3

import sys


def acyclic(adj):
    # Mark all the vertices as not visited and not part of recusion stack
    visited = [0 for _ in range(len(adj))]
    rec_stack = [0 for _ in range(len(adj))]
    # call the recursive helper function to detect cycle in different DFS Trees.
    for i in range(len(adj)):
        if not visited[i]:
            if dfs(adj, i, visited, rec_stack):
                return 1
    return 0


def dfs(adj, x, visited, rec_stack):
    # Mark the current node as visited and part of recursion stack
    visited[x] = 1
    rec_stack[x] = 1
    # Recur for all the vertices adjacent to this vertex
    for i in range(len(adj[x])):
        if not visited[adj[x][i]] and dfs(adj, adj[x][i], visited, rec_stack):
            return 1
        elif rec_stack[adj[x][i]]:
            return 1
    rec_stack[x] = 0  # remove the vertex from recursion stack
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
