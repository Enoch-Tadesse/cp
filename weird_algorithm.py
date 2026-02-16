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
    ans = []
    while n > 1:
        ans.append(n)
        if n % 2 == 0: n //= 2
        else: n = n * 3 + 1
    ans.append(1)
    print(*ans)



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
