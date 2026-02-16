import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    counter = 0
    while n > 0:
        freq = 0
        while 3 ** (freq + 1) <= n:
            freq += 1
        counter += 3 ** (freq + 1) + freq * 3 ** (freq - 1)
        n -= 3**freq
    print(int(counter))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
