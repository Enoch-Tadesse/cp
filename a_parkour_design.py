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
    x, y = list(map(int, input().split()))
    if y > 0:
        x -= y * 2
    if y < 0:
        x += 4 * y
    print("YES" if x >= 0 and x % 3 == 0 else "NO")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
