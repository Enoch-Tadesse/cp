import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))

    nums = list(map(int, input().split()))
    nums.sort()

    ans = max(nums[0], k - nums[-1])
    for i in range(1, n):
        ans = max(ans, (nums[i] - nums[i - 1]) / 2)
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
