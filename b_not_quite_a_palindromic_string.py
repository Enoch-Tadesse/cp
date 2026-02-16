import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    nums = list(x for x in input().strip())

    ones = 0
    for num in nums:
        if num == "1":
            ones += 1
    zeros = n - ones
    # _min = max(ones, zeros) - n // 2
    _min = abs(ones - zeros) // 2
    _max = ones // 2 + zeros // 2
    if _min <= k <= _max and _min & 1 == k & 1:
        print("YES")
    else:
        print("NO")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
