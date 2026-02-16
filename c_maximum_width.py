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
    n , m = list(map(int, input().split()))
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    s = s[::-1]
    t = t[::-1]

    fort = 0
    ans = 0
    fors = 0

    while fors < n and fort < m:
        
    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
