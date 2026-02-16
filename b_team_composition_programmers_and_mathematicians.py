import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    a, b = list(map(int, input().split()))
    _min = min(a, b)
    l , r = 0 , _min
    while l <= r:
        mid = l + (r - l) // 2
        if a + b >= mid * 4:
            l = mid + 1
        else:
            r = mid - 1
    print(r)



def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
