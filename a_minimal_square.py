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
    if n > m:
        n , m = m , n
    if n + n <= m:
        print(m ** 2)
        return
    n *= 2
    m *= 2
    print(min(n ** 2, m ** 2))


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
