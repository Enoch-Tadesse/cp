import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m = list(map(int, input().split()))
    tower1 = list(x for x in input().strip())
    tower2 = list(x for x in input().strip())
    tower2.reverse()
    tower1.extend(tower2)
    count = 0
    for r in range(n + m - 1):
        if tower1[r] == tower1[r + 1]:
            count += 1
    if count > 1:
        print("NO")
    else:
        print("YES")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
