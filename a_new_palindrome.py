import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def solve():
    s = list(x for x in input().strip())
    cnt = Counter(s)
    c = sum(v > 1 for v in cnt.values())
    print("YES" if c > 1 else "NO")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
