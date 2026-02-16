import sys

# sys.setrecursionlimit(10**6)
from collections import *
from math import *
from bisect import bisect_left, bisect_right
from heapq import *
from copy import deepcopy
from random import randint

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        cnt[a] += 1
        cnt[b] += 1
    first, second = "Ayush", "Ashish"

    if cnt[k] <= 1:
        print(first)
        return

    print(second if n & 1 else first)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
