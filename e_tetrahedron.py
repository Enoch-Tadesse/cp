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

mod = 10 ** 9 + 7

def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    a, b = 1, 0
    for _ in range(n):
        a, b = (b * 3) % mod , (b * 2 + a) % mod
    print(a)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
