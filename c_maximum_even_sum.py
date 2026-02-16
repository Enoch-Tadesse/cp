import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m = list(map(int, input().split()))
    if n % 2 and m % 2:
        print( n * m + 1)
        return
    if n % 2 == 0 and m % 2:
        print(-1)
        return
    if n % 2 and m % 4:
        print(-1)
        return

    print((n * m // 2) + 2)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
