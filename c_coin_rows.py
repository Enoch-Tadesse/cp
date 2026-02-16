import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    second = list(map(int, input().split()))
    second = second[::-1]
    suf = [0]
    sm = [0]
    for s in second:
        suf.append(suf[-1] + s)
        sm.append(max(sm[-1], suf[-1]))
    suf = suf[::-1]
    sm = sm[::-1]

    first = list(map(int, input().split()))
    pre = [0]
    pm = [0]
    for f in first:
        pre.append(pre[-1] + f)
        pm.append(max(pm[-1], pre[-1]))
    ans = float("inf")
    for i in range(n):
        ans = min(ans, max(pm[i], sm[i + 1]))
    print(ans)
    
    





def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
