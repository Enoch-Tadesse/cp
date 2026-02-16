import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    nums1 = set(list(map(int, input().split())))
    nums2 = set(list(map(int, input().split())))
    awb = len(nums1 - nums2)
    bwa = len(nums2 - nums1)
    print(2 * min(awb, bwa) + (2 if bwa < awb else 1))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
