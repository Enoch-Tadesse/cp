import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def check(n, t, f, s):
    return t * 3 + f * 5 + s * 7 == n


def solve():
    n = int(input())
    for t in range(n // 3 + 1):
        for f in range(n // 5 + 1):
            for s in range(n // 7 + 1):
                sum = t + f + s
                if sum > n:
                    break
                a, b, c = t, f, s
                if check(n, a, b, c):
                    print(a, b, c)
                    return
    print(-1)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
