# python3
import sys

NA = -1


class Node:
    def __init__(self):
        self.next = [NA] * 4


def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    index = 1

    for pattern in patterns:
        current = tree[0]
        for letter in pattern:
            if letter in current.keys():
                current = tree[current[letter]]
            else:
                current[letter] = index
                tree[index] = {}
                current = tree[index]
                index = index + 1
    return tree


def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    #  write your code here
    n = len(text)
    for i in range(n):
        if prefix_trie_matching(text[i:], trie):
            result.append(i)
    return result


def prefix_trie_matching(text, trie):
    idx = 0
    symbol = text[idx]
    current = trie[0]

    while True:
        if not current:
            return True
        elif symbol in current.keys():
            current = trie[current[symbol]]
            idx = idx + 1
            if idx < len(text):
                symbol = text[idx]
            else:
                symbol = '@'
        else:
            return False


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
