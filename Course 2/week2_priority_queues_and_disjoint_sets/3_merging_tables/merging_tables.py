# python3
import sys
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank, parent, ans = [1] * n, list(range(0, n)), max(lines)


def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination == realSource:
        return False
    global ans
    if rank[realDestination] <= rank[realSource]:
        realDestination, realSource = realSource, realDestination
        if rank[realDestination] == rank[realSource]:
            rank[realDestination] += 1
    parent[realSource] = realDestination
    lines[realDestination] += lines[realSource]
    lines[realSource] = 0
    ans = max(ans, lines[realDestination])
    return True


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)


# class Database:
#     def __init__(self, row_counts):
#         self.row_counts = row_counts
#         self.max_row_count = max(row_counts)
#         n_tables = len(row_counts)
#         self.ranks = [1] * n_tables
#         self.parents = list(range(n_tables))

#     def merge(self, src, dst):
#         src_parent = self.get_parent(src)
#         dst_parent = self.get_parent(dst)

#         if src_parent == dst_parent:
#             return False

#         # merge two components
#         # use union by rank heuristic
#         # update max_row_count with the new maximum table size
#         return True

#     def get_parent(self, table):
#         # find parent and compress path
#         if table != parent[table]: parent[table] = getParent(parent[table])
#         return self.parents[table]


# def main():
#     n_tables, n_queries = map(int, input().split())
#     counts = list(map(int, input().split()))
#     assert len(counts) == n_tables
#     db = Database(counts)
#     for i in range(n_queries):
#         dst, src = map(int, input().split())
#         db.merge(dst - 1, src - 1)
#         print(db.max_row_count)


# if __name__ == "__main__":
#     main()
