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
    if n == 1 and k == 10:
        print(-1)
        return 
    nums = [str(k)]
    for i in range(n - 1):
        nums.append("0")
    if k == 10:
        nums.pop()
    print("".join(nums))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
