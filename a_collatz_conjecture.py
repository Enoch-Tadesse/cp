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
    k, x = list(map(int, input().split()))
    print(x * pow(2, k))


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
