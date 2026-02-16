import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def check(nums):
    e, o = 0, 0
    for i, num in enumerate(nums):
        if i & 1:
            o ^= num
        else:
            e ^= num
    print(e == o, e, o)
    # print(e, o)


def solve():
    n = int(input())
    ans = list(range(1, n - 2))
    ans.append(1 << 29)
    ans.append(1 << 30)
    a = 0
    for i in range(len(ans)):
        a ^= ans[i]
    ans.append(a)
    print(*ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
