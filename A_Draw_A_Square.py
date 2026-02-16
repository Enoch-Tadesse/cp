import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

input = input


def solve():
    l, r, d, u = list(map(int, input().split()))

    print("Yes" if l == r == d == u else "No")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
