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
    cnt = 0
    i = 0
    while i < n - 1:
        if nums[i] == 7 - nums[i + 1] or nums[i] == nums[i + 1]:
            cnt += 1
            i += 1
        i += 1
    print(cnt)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
