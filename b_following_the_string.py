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
    _max = max(nums) + 1
    arr = [[] for _ in range(_max)]

    for i in range(n):
        arr[nums[i]].append(i)

    chars = [chr(ord("a") + i) for i in range(26)]
    ans = [""] * n

    pointer = 0

    for i in range(len(arr[0])):
        for j in range(_max):
            if len(arr[j]) <= i:
                break
            ans[arr[j][i]] = chars[pointer]

        pointer += 1

    print("".join(ans))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
