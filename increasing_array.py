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
    nums = list(map(int, input().split()))
    last = -1 
    ans = 0
    for num in nums:
        if num < last:
            ans += last - num
        else:
            last = num
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
