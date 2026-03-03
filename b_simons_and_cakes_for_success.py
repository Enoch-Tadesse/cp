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
    n = int(input())
    ans = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            ans *= i
        while n % i == 0:
            n //= i
        i += 1
    if n > 1:
        ans *= n
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
