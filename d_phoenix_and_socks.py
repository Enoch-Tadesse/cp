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


def calculator(nums, l, r):
    cost = 0
    nums = sorted([v for _, v in nums.items()], reverse=True)
    trans_change = l
    for i in range(len(nums)):
        while nums[i] > 1 and l != r:
            nums[i] -= 2
            cost += 1
            r += 1
            l -= 1
            trans_change -= 2
        if l == r:
            break
    return cost + trans_change


def solve():
    n, l, r = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    left = Counter(nums[:l])
    right = Counter(nums[l:])

    for sock in list(left.keys()):
        if sock in right:
            size = min(left[sock], right[sock])
            left[sock] -= size
            right[sock] -= size

            l -= size
            r -= size

            if left[sock] == 0:
                del left[sock]
            if right[sock] == 0:
                del right[sock]

    if l == r:
        print(l)
    elif l > r:
        print(calculator(left, l, r))
    else:
        print(calculator(right, r, l))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
