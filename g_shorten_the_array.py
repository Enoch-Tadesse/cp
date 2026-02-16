class TrieNode:
    def __init__(self):
        self.child = [None, None]
        self.idx = 0
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.mx = 45

    def insert(self, val, idx):
        node = self.root
        for i in range(self.mx - 1, -1, -1):
            bit = (val >> i) & 1
            if not node.child[bit]:
                node.child[bit] = TrieNode()
            node = node.child[bit]
            node.count += 1
        node.idx = idx

    def max_xor(self, val, k):
        node = self.root
        if not node:
            return 0
        ans = 0
        for i in range(self.mx - 1, -1, -1):
            b = (val >> i) & 1
            tog = 1 - b
            if node.child[tog] and node.child[tog].count > 0:
                ans |= 1 << i
                node = node.child[tog]
            elif node.child[b]:
                node = node.child[b]
            else:
                break

        if ans >= k:
            return node.idx
        return -1

    def remove(self, val):
        node = self.root
        path = []
        for i in range(self.mx - 1, -1, -1):
            bit = (val >> i) & 1
            if not node.child[bit]:
                return
            node = node.child[bit]
            path.append(node)

        node = self.root
        for i in range(self.mx - 1, -1, -1):
            bit = (val >> i) & 1
            nxt = node.child[bit]
            nxt.count -= 1
            if nxt.count == 0:
                node.child[bit] = None
                return
            node = nxt


import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    t = Trie()
    l = 0
    ans = 10**6

    for r in range(n):
        t.insert(a[r], r)
        while l <= r:
            nl = t.max_xor(a[r], m)
            if nl == -1:
                break
            ans = min(ans, r - l + 1)
            t.remove(a[l])
            l += 1

    print(-1 if ans == 10**6 else ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
