import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m = list(map(int, input().split()))
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    s = []
    i, j = 0, 0
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            s.append(nums1[i])
            i += 1
        else:
            s.append(nums2[j])
            j += 1
    s.extend(nums1[i:])
    s.extend(nums2[j:])
    print(*s)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
