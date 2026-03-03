import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    a = list(x for x in input().strip())
    b = list(x for x in input().strip())

    prea = [[0] * 26]
    preb = [[0] * 26]

    for j in range(n):
        c = a[j]
        i = ord(c) - ord("a")
        last = prea[-1][::]
        last[i] += 1
        prea.append(last)

        c = b[j]
        i = ord(c) - ord("a")
        last = preb[-1][::]
        last[i] += 1
        preb.append(last)

    for _ in range(k):
        l, r = list(map(int, input().split()))
        l -= 1
        first = []
        second = []
        for i in range(26):
            first.append(prea[r][i] - prea[l][i])
            second.append(preb[r][i] - preb[l][i])
        diff = 0
        for i in range(26):
            diff += abs(first[i] - second[i])
        print(diff // 2)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
