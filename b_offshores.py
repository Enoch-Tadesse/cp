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
    n, x, y = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    ans = 0
    print(nums)
    for i in range(n - 1, 0, -1):
        print(nums)

        nums[i] = (nums[0] // x) * y + nums[i]
        nums[0] = nums[i]
    print(nums)
    


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
