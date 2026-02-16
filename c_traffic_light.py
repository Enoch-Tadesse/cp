import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, target = list(map(str, input().split()))

    chars = list(x for x in input().strip())

    n = int(n)
    if target == "g":
        print(0)
        return
    chars += chars

    gs = []
    for i, c in enumerate(chars):
        if c == "g":
            gs.append(i)

    def finder(start):
        k = bisect_right(gs, start)
        if k >= len(gs):
            return -1
        return abs(gs[k] - start)

    ans = 0
    for i, c in enumerate(chars):
        if c == target:
            ans = max(ans, finder(i))
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
