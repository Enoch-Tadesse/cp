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


def calc(chars):
    ans = 0
    total = chars.count(chars[0])
    res = 0

    for i in range(total, len(chars)):
        res += chars[0] == chars[i]
    return res

    # l = 0
    # r = len(chars) - 1
    # while l < r:
    #     while l < r and chars[l] == target:
    #         l += 1
    #     while l < r and chars[r] != target:
    #         r -= 1
    #     if l != r:
    #         chars[l], chars[r] = chars[r], chars[l]
    #         ans += 1
    # return ans


def solve():
    n = int(input())
    chars = list(x for x in input().strip())
    chars += chars

    ans = float("inf")
    for i in range(len(chars) - n):
        test = chars[i : i + n]
        ans = min(ans , calc(test))
        # ans = min(ans, calc(test[::], "H"))
        # ans = min(ans, calc(test[::], "T"))
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
