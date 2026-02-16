import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    nums = input().strip()
    nums2 = nums.split("+")
    nums2.sort()
    print("+".join(nums2))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
