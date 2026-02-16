import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    counter = 0
    for i in range(1, n ):
        if (n - i) % i == 0:
            counter += 1
    print(counter)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
