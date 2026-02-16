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
    if n == 0:
        print(1)
        return
    ans = [6, 8, 4, 2, 6]
    print(ans[n % 4])

    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
