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

def counter(s):
    n = len(s)
    l = r = cnt = 0
    while r < n:
        if s[r] == s[l]:
            r += 1
            continue
        l = r
        cnt += 1
    return cnt + 1


def solve():
    n = int(input())
    s = input().strip()
    s += s

    ans = 0
    for i in range(len(s) - n):
        c = s[i:i + n]
        ans = max(ans, counter(c))
    print(ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
