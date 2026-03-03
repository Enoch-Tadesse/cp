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
    nums.sort()
    last = 1
    cnt = 0
    for num in nums:
        if num >= last:
            cnt += 1
            last = num + 1
    print(cnt)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
