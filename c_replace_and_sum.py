import sys
# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *

# input = input
input = sys.stdin.readline


def solve():
    n , q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [max(a[i], b[i]) for i in range(n)]

    for i in range(n - 2, -1, -1):
        c[i] = max(c[i], c[i + 1])

    pre = [0]
    for d in c:
        pre.append(pre[-1] + d)

    for _ in range(q):
        a, b = list(map(int, input().split()))
        print(pre[b] - pre[a - 1])


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
