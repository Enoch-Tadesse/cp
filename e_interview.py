import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def log(l, r):
    print("?", (r - l + 1), *list(range(l, r + 1)), flush=True)
    return int(input())


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    pre = [0]
    for num in nums:
        pre.append(num + pre[-1])
    l, r = 1, n
    while l < r:
        mid = (l + r) // 2

        if pre[mid] - pre[l - 1] == log(l, mid):
            l = mid + 1
        else:
            r = mid
    print("!", l, flush=True)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
