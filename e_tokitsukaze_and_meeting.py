import sys, threading
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right, insort
import random
import math
from heapq import heapify, heappush, heappop
from random import getrandbits
from itertools import accumulate
from functools import reduce
from operator import (
    add,
    sub,
    mul,
    truediv,
    floordiv,
    mod,
    pow,
    neg,
    and_,
    or_,
    xor,
    inv,
    lshift,
    rshift,
)

RANDOM = getrandbits(32)
MOD = 10**9 + 7
inf = float("inf")


def precision(val, x):
    return f"{val:.{x}f}"


class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


def solve():
    n, m = map(int, sys.stdin.readline().split())
    s = input()

    gl = [0] * n * m

    def helper(s, n, m):
        ans = [0] * n * m
        arr = [0] * m
        for i in range(n * m):
            ans[i] = ans[i - 1]
            if arr[(i) % m] == 0 and s[i] == "1":
                ans[i] += 1
            arr[(i) % m] |= int(s[i])

        return ans

    res = helper(s, n, m)
    for i in range(n * m):
        gl[i] += res[i]

    def row(s, n, m):
        ans = [0] * n * m
        arr = [0] * n
        for i in range(n * m - 2, -1, -1):
            ans[i] = ans[i + 1]
            if arr[(i) % n] == 0 and s[i] == "1":
                ans[i] += 1
            arr[(i) % n] |= int(s[i])

        return ans[::-1]

    x = row(s, n, m)
    print("row", *x)

    return gl


for _ in range(int(sys.stdin.readline().strip())):
    print("col", *solve())
