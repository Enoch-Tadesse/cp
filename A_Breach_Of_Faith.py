import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

input = input


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    out = [nums.pop()]
    acc = 0
    for i in range(len(nums) - 1):
        if i & 1:
            acc -= nums[i]
        else:
            acc += nums[i]
        out.append(nums[i])
    x = out[0] - acc + nums[-1]
    out.append(x)
    out.append(nums[-1])
    print(*out)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
