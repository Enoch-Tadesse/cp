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
    if n & 1:
        print(-1)
        return
    for i in range(1, n + 1, 2):
        print(i+1, i, end=" ")
    print()


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
