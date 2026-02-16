import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    a, b , c , d = list(map(int, input().split()))
    big = max(a, b)
    small = min(a, b)
    while big > 1 and small > 0:
        big -= 2
        small -= 1
    if big - small > 2:
        print("NO")
        return
    big = max(c - a, d - b)
    small = min(c- a, d - b)
    while big > 1 and small > 0:
        big -= 2
        small -= 1
    if big - small > 2:
        print("NO")
        return
    print("YES")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
