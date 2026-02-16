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
    counts = [0] * 1002
    for num in nums:
        counts[num] += 1
    for i in range(1001):
        c = counts[i]
        if c == 1:
            print("No")
            return
        if c == 0:
            continue
        counts[i + 1] += (c - 2)
    print("Yes")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
