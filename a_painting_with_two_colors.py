import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, a, b = list(map(int, input().split()))
    if a > b:
        if (n - a) & 1 != 0 or (a - b) & 1 != 0:
            print("NO")
        else:
            print("YES")
        return
    print("NO" if (n - b) & 1 else "YES")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
