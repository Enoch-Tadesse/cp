import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    op = list(x for x in input().strip())
    
    ans = ["?"] * n
    l, r = 0, n - 1
    counter = 0
    for o in op:
        if o == "0":
            ans[l] = "-"
            l += 1
        elif o == "1":
            ans[r] = "-"
            r -= 1
        else:
            counter += 1
    remain = r - l
    print("".join(ans))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
