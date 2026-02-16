import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    weights = list(map(int, input().split()))
    nums = weights[::]
    nums.sort()
    pre = []
    run = 0
    for num in nums:
        pre.append(run)
        run += num
    r = n - 2
    while r >= 0:  # as soon as it detects a loser, it stops
        find = nums[r + 1] - nums[r]
        if find == 0:
            r -= 1
            continue
        if pre[r] < find:
            break
        r -= 1
    if r == -1:  # if there is no loser
        print(len(nums))
        print(*[i + 1 for i in range(len(nums))])
    else:  # print every guy strictly bigger than the loser
        loser = nums[r]
        print(len(nums) - r - 1)
        for i, num in enumerate(weights):
            if num > loser:
                print(i + 1, end=" ")
        print()


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
