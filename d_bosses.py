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
    par = {i : i for i in range(1, n + 1)}
    for _ in range(m):



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
