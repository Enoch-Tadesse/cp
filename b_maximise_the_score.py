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
    ans = 0
    for i in range(0 , 2 * n , 2):
        ans += min(nums[i] , nums[i + 1])
    print(ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
