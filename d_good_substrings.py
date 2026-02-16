import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


# ---------- Trie Implementation (Lazy Deletion with Count) ----------
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        self.count = 0


class Trie:
    def __init__(self, goods):
        self.root = TrieNode()
        self.goods = goods
        self.ans = 0

    def _char_to_index(self, ch):
        return ord(ch) - ord("a")

    def insert(self, word, l, k):
        curr = 0
        node = self.root
        ans = 0
        for i in range(l, len(word)):
            ch = word[i]
            idx = self._char_to_index(ch)
            curr += not self.goods[idx]
            if not node.children[idx]:
                node.children[idx] = TrieNode()
                ans += curr <= k
            node.count = curr
            node = node.children[idx]
            if curr > k:
                self.ans += ans
                return
        node.is_end = True
        self.ans += ans

    def query(self, word):
        node = self.root
        for ch in word:
            idx = self._char_to_index(ch)
            child = node.children[idx]
            if not child or child.count == 0:
                return False
            node = child
        return node.is_end

    def delete(self, word):
        node = self.root
        path = []

        for ch in word:
            idx = self._char_to_index(ch)
            child = node.children[idx]
            if not child or child.count == 0:
                return  # word not found
            path.append(child)
            node = child

        if not node.is_end:
            return

        node.is_end = False
        for child in path:
            child.count -= 1


def solve():
    chars = list(x for x in input().strip())
    goods = list(int(x) for x in input().strip())
    k = int(input())
    trie = Trie(goods)
    for i in range(len(chars)):
        trie.insert(chars, i, k)
    print(trie.ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
