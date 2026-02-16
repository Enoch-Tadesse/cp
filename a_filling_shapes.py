import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    if n & 1:
        print(0)
    else:
        print(2 ** (n // 2))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
