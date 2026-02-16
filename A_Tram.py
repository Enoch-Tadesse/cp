import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = sys.stdin.readline


def solve():
    counter = 0
    res = -1
    n = int(input())
    for _ in range(n):
        d, i = list(map(int, input().split()))
        counter += i - d
        res = max(res, counter)
    print(res)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
