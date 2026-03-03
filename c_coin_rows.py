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
    for s in second:
        suf.append(suf[-1] + s)
    suf = suf[::-1]

    first = list(map(int, input().split()))
    pre = [0]
    for f in first:
        pre.append(pre[-1] + f)

    ans = float("inf")
    for i in range(n):
        ans = min(ans, max(pre[i], suf[i + 1]))
    print(ans)
    
    





def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
