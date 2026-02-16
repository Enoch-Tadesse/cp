import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    print(4 - len(set(list(map(int, input().split())))))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
