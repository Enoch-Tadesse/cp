import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    home = dict()
    away = dict()
    teams = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        home[i] = a
        away[i] = b
    counter = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if home[i] == away[j]:
                counter += 1
            if home[j] == away[i]:
                counter += 1
    print(counter)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
