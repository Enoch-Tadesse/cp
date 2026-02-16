import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    string = input().strip()

    cnt = string.count("1")
    counter = (n - cnt) * (cnt + 1)
    counter += (cnt) * (cnt - 1)
    print(counter)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
