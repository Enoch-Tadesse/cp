# 4 5 1 7 2 6 3

import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    if n <= 4:
        print(-1)
        return
    odds, evens = [], []
    for i in range(1, n + 1):
        if i & 1:
            if i != 5: odds.append(i)
        else:
            if i != 4: evens.append(i)
    evens.reverse()
    print(*odds, 5, 4, *evens)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
