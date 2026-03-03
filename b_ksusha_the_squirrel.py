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
    n , k = list(map(int, input().split()))
    s = input().strip()
    chars = s.split(".")
    for c in chars:
        if len(c) >= k:
            print("NO")
            return
    print("YES")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
