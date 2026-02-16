import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


ans = [[] for _ in range(17)]
ans[1] = [1, 0]

for i in range(2, 17):
    res = 1 << (i - 1)
    ans[i].extend([(x << 1) | 1 for x in ans[i - 1]])
    ans[i].extend([j << 1 for j in range(res)])

for i in range(16):
    print(ans[i])


def solve():
    n = int(input())
    print(*ans[n])


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
