import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = sys.stdin.read

n, q = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))

nums.sort(reverse=True)

for i in range(1, n):
    nums[i] += nums[i - 1]

for _ in range(q):
    x, y = list(map(int, sys.stdin.readline().split()))
    x -= 1
    diff = x - y
    print(nums[x] - nums[diff] if diff >= 0 else nums[x])

    # print(f"{x=} {diff=}")
