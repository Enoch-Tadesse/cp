import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , k = list(map(int, input().split()))
    colors = list(x for x in input().strip())
    l = 0
    ans = 0
    out = float("inf")
    for r in range(n):
        if r - l + 1 < k:
            ans += colors[r] == "W"
            continue
        ans += colors[r] == "W"
        out = min(ans, out)
        ans -= colors[l] == "W"
        l += 1
    print(out)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
