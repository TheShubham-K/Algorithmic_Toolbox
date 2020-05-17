# python3


# def build_heap(data):
"""Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
# The following naive implementation just sorts the given sequence
# using selection sort algorithm and saves the resulting sequence
# of swaps. This turns the given array into a heap, but in the worst
# case gives a quadratic number of swaps.
#
# TODO: replace by a more efficient implementation
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps


# def main():
#     n = int(input())
#     data = list(map(int, input().split()))
#     assert len(data) == n

#     swaps = build_heap(data)

#     print(len(swaps))
#     for i, j in swaps:
#         print(i, j)


# if __name__ == "__main__":
#     main()
n = None


class HeapBuilder:

    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        global n
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def SiftDown(self, i):
        minIndex = i
        left = 2 * i + 1
        if left < n and self._data[left] < self._data[minIndex]:
            minIndex = left
        right = 2 * i + 2
        if right < n and self._data[right] < self._data[minIndex]:
            minIndex = right
        if i != minIndex:
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            self._swaps.append([i, minIndex])
            self.SiftDown(minIndex)

    def GenerateSwaps(self):
        for i in range(n // 2, -1, -1):
            self.SiftDown(i)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
