# python3

import sys
import threading
from collections import deque, defaultdict
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        # maxHeight = 0
        # for vertex in range(self.n):
        #         height = 0
        #         i = vertex
        #         while i != -1:
        #                 height += 1
        #                 i = self.parent[i]
        #         maxHeight = max(maxHeight, height);
        # return maxHeight;
        nodes = defaultdict(set)
        for i in range(self.n):
            if self.parent[i] == -1:
                root = i
            else:
                nodes[self.parent[i]].add(i)
        if nodes == None:
            return
        q, level, target, active = deque([root]), 0, root, 0
        while q:
            node = q.popleft()
            if node == target:
                level, active = level + 1, 1
            if nodes[node] != []:
                for i, child in enumerate(nodes[node]):
                    q.append(child)
                if active == 1 and q:
                    target, active = q[-1], 0
        return level

# This is also Another way to done

# class TreeHeight:
#     def read(self):
#         self.n = int(sys.stdin.readline())
#         self.parent = list(map(int, sys.stdin.readline().split()))

#         self.nodes = []
#         self.root = None

#         self.nodes = [[] for i in range(self.n)]

#         for child_index in range(self.n):
#             parent_index = self.parent[child_index]
#             if parent_index == -1:
#                 self.root = child_index
#             else:
#                 self.nodes[parent_index] += [child_index]


#     def compute_height(self):
#         queue = []
#         height = 0
#         queue.append(self.root)

#         while True:
#             node_count = len(queue)
#             if node_count == 0:
#                 return height
#             height += 1
#             while node_count > 0:
#                 node = queue.pop(0)
#                 if self.nodes[node]:
#                     for x in self.nodes[node]:
#                         queue.append(x)
#                 node_count -= 1


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
