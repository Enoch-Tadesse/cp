import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = input


def solve():
    n = int(input())
    nums1 = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))

    for i in range(1, n):
        nums1[i] += nums1[i - 1]
    for i in range(1, m):
        nums2[i] += nums2[i - 1]
    print(max(max(nums1), 0) + max(max(nums2), 0))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
