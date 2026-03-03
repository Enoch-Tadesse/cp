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
    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))
    last = max(nums[0])
    for i in range(1, n):
        nxt = 0
        a, b = nums[i]
        flag = False
        if a <= last:
            nxt = max(a, nxt)
            flag = True
        if b <= last:
            nxt = max(b, nxt)
            flag = True
        last = nxt
        if not flag:
            print("NO")
            return
    print("YES")

    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
