import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    ans = 0
    l = 0
    r = n - 1
    while l <= r:
        curr = 0
        while l <= r and curr + nums[r] <= 4:
            curr += nums[r]
            r -= 1
        while l <= r and curr + nums[l] <= 4:
            curr += nums[l]
            l += 1
        ans += 1
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
