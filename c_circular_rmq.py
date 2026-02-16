class Segment:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [float("inf")] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def leftPos(self, pos):
        return (pos << 1) + 1

    def rightPos(self, pos):
        return (pos << 1) + 2

    def build(self, pos, l, r):
        if l == r:
            self.tree[pos] = self.nums[l]
            return

        mid = (l + r) // 2
        self.build(self.leftPos(pos), l, mid)
        self.build(self.rightPos(pos), mid + 1, r)
        self.tree[pos] = min(self.tree[self.leftPos(pos)], self.tree[self.rightPos(pos)])

    def push(self, pos, l, r):
        if self.lazy[pos] != 0:
            self.tree[pos] += self.lazy[pos]
            if l != r:
                self.lazy[self.leftPos(pos)] += self.lazy[pos]
                self.lazy[self.rightPos(pos)] += self.lazy[pos]
            self.lazy[pos] = 0

    def updateHelper(self, pos, l, r, val, L, R):
        self.push(pos, l, r)
        if r < L or l > R:
            return
        if l >= L and r <= R:
            self.lazy[pos] += val
            self.push(pos, l, r)
            return
        mid = (l + r) // 2
        self.updateHelper(self.leftPos(pos), l, mid, val, L, R)
        self.updateHelper(self.rightPos(pos), mid + 1, r, val, L, R)

        self.tree[pos] = min(
            self.tree[self.leftPos(pos)], self.tree[self.rightPos(pos)]
        )

    def queryHelper(self, pos, l, r, L, R):
        self.push(pos, l, r)
        if l > R or r < L:
            return float("inf")
        if l >= L and r <= R:
            return self.tree[pos]
        mid = (l + r) // 2
        return min(
            self.queryHelper(self.leftPos(pos), l, mid, L, R),
            self.queryHelper(self.rightPos(pos), mid + 1, r, L, R),
        )


import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    seg = Segment(nums)
    for _ in range(m):
        op = list(map(int, input().split()))
        l, r = op[0], op[1]
        if len(op) == 3:
            if l > r:
                seg.updateHelper(0, 0, n - 1, op[2], l, n - 1)
                seg.updateHelper(0, 0, n - 1, op[2], 0, r)
            else:
                seg.updateHelper(0, 0, n - 1, op[2], l, r)
        else:
            if l > r:
                print(
                    min(
                        seg.queryHelper(0, 0, n - 1, l, n - 1),
                        seg.queryHelper(0, 0, n - 1, 0, r),
                    )
                )
            else:
                print(seg.queryHelper(0, 0, n - 1, l, r))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
