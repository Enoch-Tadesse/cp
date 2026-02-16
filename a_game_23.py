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
    a, b = list(map(int, input().split()))
    if b % a != 0:
        print(-1)
        return
    d = b // a
    ans = 0
    while d % 3 == 0:
        d //= 3
        ans += 1
    while d % 2 == 0:
        d //= 2
        ans += 1
    if d != 1:
        print(-1)
    else:
        print(ans)




def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
