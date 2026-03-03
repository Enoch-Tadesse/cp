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
    nums = list(map(int, input().split()))
    nums = [(num , i + 1) for i , num in enumerate(nums)]
    nums.sort()
    curr = 0
    ans = []
    for r in range(n):
        curr += nums[r][0]
        if curr <= k:
            ans.append(nums[r][1])
        else:
            break

    if ans:
        print(len(ans))
        print(*ans)
    else: print(0)
    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
