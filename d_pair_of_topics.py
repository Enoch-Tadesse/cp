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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # ai + aj > bi + bj
    # ai - bi > bj - aj
    first = [a[i] - b[i] for i in range(n)]
    second = [b[j] - a[j] for j in range(n)]
    print(first)
    print(second)
    # for every first now, how many numbers to the right are greater than it


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
