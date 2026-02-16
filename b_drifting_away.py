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
    s = input().strip()
    if len(s) == 1:
        print(1)
        return
    # *< , >*, **,
    if "*<" in s or ">*" in s or "**" in s or "><" in s:
        print(-1)
    else:
        # <<<<<<<<<<<<<*********>>>>>>>>>
        ans = 0
        i = 0
        while i < len(s) and s[i] == "<":
            i += 1

        extra = 0

        if i < len(s) and s[i] == "*":
            extra = 1
            i += 1

        ans = max(extra + len(s) - i, i)
        print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
