import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    y, b = list(map(int, input().split()))
    counts = 0
    while y <= b:
        y *= 3
        b *= 2
        counts += 1
    print(counts)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
