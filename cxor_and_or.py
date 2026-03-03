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
    top = list(x for x in input().strip())
    bot = list(x for x in input().strip())

    if len(top) != len(bot):
        print("NO")
        return

    b1 = bot.count("1")
    t1 = top.count("1")

    if b1 == 0:
        print("YES" if not t1 else "NO")
    else:
        print("YES" if t1 else "NO")
    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
