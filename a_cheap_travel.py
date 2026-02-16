import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , c, o, m = list(map(int, input().split()))

    if c >= m:
        print(n)
        return
    p1 = 1 / o
    p2 = c / m

    if p1 < p2:
        

    else:
    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
