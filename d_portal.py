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


def calc(s):

    n = len(s)
    if n <= 1:
        return s

    _min = min(s)
    i = s.index(_min)
    ans = []
    for j in range(i, i + n):
        ans.append(s[j % n])
    return ans


def _min(a, b):
    for i in range(len(a)):
        if a[i] < b[i]:
            return a
        elif a[i] > b[i]:
            return b
    return a


def solve():
    n, x, y = list(map(int, input().split()))

    nums = list(map(int, input().split()))

    if x == y:
        print(*nums)
        return

    mid = nums[x:y]
    mid = calc(mid)
    left = nums[:x]
    right = nums[y:]
    ans = left + mid + right

    if left:
        coll = []
        x = left[::]
        while left and left[-1] > mid[0]:
            coll.append(left.pop())
        coll = coll [::-1]
        ans = _min(ans, left + mid + coll + right)
        left = x

    if right:
        right = right[::-1]
        coll = []
        while right and right[-1] < mid[0]:
            coll.append(right.pop())
        right = right[::-1]
        ans = _min(ans, left + coll + mid + right)

    print(*ans)




def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()

