import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.child = [None, None]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        curr = self.root
        for bit in range(46, -1, -1):
            b = (num >> bit) & 1
            if not curr.child[b]:
                curr.child[b] = TrieNode()
            curr = curr.child[b]

    def query(self, num):
        node = self.root
        if not node:
            return 0
        ans = 0
        for bit in range(46, -1, -1):
            b = (num >> bit) & 1
            tog = 1 ^ b
            if node.child[tog]:
                ans |= 1 << bit
                node = node.child[tog]
            else:
                node = node.child[b]
        return ans


def solve():
    n = int(input().strip())
    a = list(map(int, input().split()))

    pre = [0] * (n + 1)
    suf = [0] * (n + 2)

    for i in range(1, n + 1):
        pre[i] = pre[i - 1] ^ a[i - 1]

    for i in range(n, 0, -1):
        suf[i] = suf[i + 1] ^ a[i - 1]

    trie = Trie()
    plea = 0
    trie.insert(pre[0])

    for j in range(1, n + 2):
        p = trie.query(suf[j])
        plea = max(plea, p)
        if j <= n:
            trie.insert(pre[j])

    print(plea)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
