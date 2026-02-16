import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def can(turns, d):


def solve():
    h, d = list(map(int, input().split()))
    l, r = d, 2 * d + 2
    while l <= r:
        mid = l + (r - l) // 2
        if can(mid, d):
            r = mid - 1
        else:
            l = mid + 1
    return l


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
