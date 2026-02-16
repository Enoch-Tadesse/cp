import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    if n <= 2:
        print(0)
        return
    a = math.ceil(n / 2)
    print(n - a if n & 1 else n - a - 1)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
