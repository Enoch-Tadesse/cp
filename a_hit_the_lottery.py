import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    opts = [100, 20, 10, 5, 1]
    counter = 0
    i = 0
    while n > 0 and i < 5:
        if n >= opts[i]:
            d = n // opts[i]
            n -= (opts[i] * d)
            counter += d
        else:
            i += 1
    print(counter)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
