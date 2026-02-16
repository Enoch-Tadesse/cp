import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    if n == 1:
        print(k)
        return
    mid = math.ceil(n / 2)
    print(k // (n - mid + 1))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
