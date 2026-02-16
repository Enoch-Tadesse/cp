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
    s, k, m = map(int, input().split())

    if k >= s:
        print(max(0, s - (m % k)))
    else:
        if (m % (2 * k)) < k:
            print(s - (m % k))
        else:
            print(k - (m % k))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
