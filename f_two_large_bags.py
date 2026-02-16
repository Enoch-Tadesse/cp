import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    _max = max(nums)
    counts = [0] * (_max + 2)
    for num in nums:
        counts[num] += 1
    for i, val in enumerate(counts):
        if val == 1:
            print("No")
            return
        if i + 1 <= _max + 1:
            counts[i + 1] += max(0, val - 2)
    print("No" if counts[-1] & 1 else "Yes")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
