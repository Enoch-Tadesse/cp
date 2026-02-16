import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
from functools import lru_cache
import math

# input = input
input = sys.stdin.readline


def solve():
    chars = list(x for x in input().strip())
    if len(chars) & 1 == 0 and chars[0] != ")" and chars[-1] != "(":
        print("YES")
    else:
        print("NO")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
