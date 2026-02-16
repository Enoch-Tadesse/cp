import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    a, b = list(map(int, input().split()))
    all = b - a + 1
    sub = [2, 3, 5, 7, 30, 42, 70, 105]
    add = [6, 10, 14, 15, 21, 35, 210]
    for s in sub:
        all -= helper(a, b, s)
    for s in add:
        all += helper(a, b, s)
    print(all)


def helper(left, right, num):
    return right // num - (left - 1) // num


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
