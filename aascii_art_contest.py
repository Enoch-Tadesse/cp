import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[-1] - nums[0] >= 10:
        print("check again")
    else:
        print("final", nums[1])


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
