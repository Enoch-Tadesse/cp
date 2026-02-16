import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    l, r = map(int, input().split())
    L, R = map(int, input().split())

    if r < L or R < l:
        print(1)
        return

    left = max(l, L)
    right = min(r, R)

    ans = right - left

    if l != L:
        ans += 1
    if r != R:
        ans += 1

    print(ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
