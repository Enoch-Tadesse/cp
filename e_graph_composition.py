import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m, k = list(map(int, input().split()))
    first = set()
    second = set()
    for _ in range(m):
        a, b = list(map(int, input().split()))
        first.add((a, b))
    for _ in range(k):
        a, b = list(map(int, input().split()))
        second.add((a, b))
    if k == 0:
        print(m)
        return
    if m == 0:
        print(k)
        return
    cnt = len(first)
    for a, b in second:
        if (a, b) in first:
            first.discard((a, b))
            cnt -= 1
        else:
            cnt += 1
    print(cnt)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
