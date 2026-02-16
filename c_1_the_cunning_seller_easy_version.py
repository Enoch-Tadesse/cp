import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def prof(x):
    return 3 ** (x + 1) + x * (3 ** (x - 1))

def solve():
    n = int(input())
    counter = 0
    while n > 0:
        times = 0
        while 3 ** (times + 1) <= n:
            times += 1
        counter += prof(times)
        n -= 3 ** times
    print(int(counter))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
