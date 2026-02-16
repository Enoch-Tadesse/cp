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
    if n == 1:
        print(k)
        return
    if k > n:
        print(int(ceil(k / 2)))
    else:
        print(int(ceil(n / 2)))


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
