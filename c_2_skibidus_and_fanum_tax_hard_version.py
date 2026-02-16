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

    nums2.sort()
    ans = [float("-inf")]
    i, j = 0, 0
    while i < n and j < m:
        take = float("inf")
        cand = nums2[j] - nums1[i]
        if cand >= ans[-1]:
            take = min(take, cand)
        if nums1[i] >= ans[-1]:
            take = min(take, nums1[i])
        if cand >= ans[-1] or nums1[i] >= ans[-1]:
            ans.append(take)
            i += 1
        else:
            j += 1
    print(ans)
    ans.extend(nums1[i:])
    print("YES" if ans == list(sorted(ans)) else "NO")
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
