import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def merge_sort(nums, call, out):
    if len(nums) <= 1:
        if len(nums) == 1:
            out.append(1)
        return
    if call[0] < 2:
        out.append(len(nums))
        return
    mid = len(nums) // 2
    call[0] -= 2
    merge_sort(nums[:mid], call, out)
    merge_sort(nums[mid:], call, out)


def solve():
    n, calls = list(map(int, input().split()))
    nums = [i for i in range(1, n + 1)]
    call = [calls]
    if call[0] % 2 == 0:
        print(-1)
        return
    call[0] -= 1
    out = []
    merge_sort(nums, call, out)
    print(len(out))
    res = []
    # start = 1
    # for ind in out[::-1]:
    #     for i in range(start + ind - 1, start - 1, -1):
    #         start += 1
    #         res.append(i)
    # res.reverse()
    print(*res)


def main():
    t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
