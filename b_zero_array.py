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
    _sum = sum(nums)
    if _sum & 1:
        print("NO")
        return
    if nums[-1] <= _sum - nums[-1]:
        print("YES")
    else:
        print("NO")


def main():
    t = 1
    for _ in range(t):
        solve()


# ab + bc + ac <=n
# a + b + c <=x
# a + b <= x - c

# ab + c(a + b) <= n

# ab + c(x - c) <= n

# ab - cc + cx <= n




if __name__ == "__main__":
    main()
