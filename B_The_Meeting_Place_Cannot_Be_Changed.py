import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def valid(time, x, v):
    left = float("-inf")
    right = float("inf")
    for i in range(len(x)):
        left = max(left, x[i] - v[i] * time)
        right = min(right, x[i] + v[i] * time)
    return left <= right


def solve():
    n = int(input())

    x = list(map(int, input().split()))
    v = list(map(int, input().split()))
    pre = 10**-6
    left = 0
    right = max(x) - min(x)
    while left <= right:
        mid = (left + right) / 2
        if valid(mid, x, v):
            right = mid - pre
        else:
            left = mid + pre
    print(left)


def main():
    t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
