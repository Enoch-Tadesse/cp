import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def merge_sort(nums, weight):
    if len(nums) <= 1:
        return (nums, 0)
    mid = len(nums) // 2
    left, l_swap = merge_sort(nums[:mid], weight)
    right, r_swap = merge_sort(nums[mid:], weight)
    res, swaps = merge(left, right, weight)
    return (res, swaps + l_swap + r_swap)


def merge(left, right, weight):
    counter = 0
    l, r = 0, 0
    res = []
    while l < len(left) and r < len(right):
        if weight[right[r]] < weight[left[l]]:
            counter += (len(left)) - l
            res.append(right[r])
            r += 1
        else:
            res.append(left[l])
            l += 1
    res.extend(left[l:])
    res.extend(right[r:])
    return (res, counter)


def solve():
    weight = dict()
    t = int(input())
    for _ in range(t):
        s, e = list(map(int, input().split()))
        weight[s] = e
    nums = sorted(weight.keys())
    res, swaps = merge_sort(nums, weight)
    print(swaps)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
