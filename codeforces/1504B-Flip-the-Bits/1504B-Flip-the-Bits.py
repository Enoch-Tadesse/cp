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
    n = int(input())
    a = list(int(x) for x in input().strip())
    b = list(int(x) for x in input().strip())
    ones = a.count(1)
    zeros = n - ones
    flip = 0
    for i in range(n - 1, -1, -1):
        a[i] ^= flip
        if a[i] != b[i]:
            if ones != zeros:
                print("NO")
                return
            zeros -= a[i] == 0
            ones -= a[i] == 1
            zeros, ones = ones, zeros
            flip ^= 1
        else:
            zeros -= a[i] == 0
            ones -= a[i] == 1
    print("YES")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()