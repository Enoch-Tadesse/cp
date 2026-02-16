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

    def calc(nums, target):
        odds, evens = 0, 0
        for num in nums:
            diff = target - num
            evens += diff // 2
            odds += diff & 1
        return odds, evens

    ans = float("inf")
    _max = max(nums)

    def helper(_max):

        o, e = calc(nums, _max)
        diff = min(o, e)
        o -= diff
        e -= diff

        curr = float("inf")
        if o != 0:
            curr = min(curr, diff * 2 + (o * 2 - ((diff) & 1)))
        if e != 0:
            temp = 0
            if diff & 1:
                temp += 1
                e -= 1
            total = e * 2
            temp += (total // 3) * 2
            curr = min(curr, diff * 2 + temp + (e % 3 != 0))

        return curr

    ans = min(ans, helper(_max), helper(_max + 1))

    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
