import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def valid(guess, time):
    t = 5 * ((guess + 1) * guess) // 2
    return time >= t


def solve():
    n, k = list(map(int, input().split()))
    allowed = 240 - k
    l, r = 0, n
    res = n
    while l <= r:
        mid = l + (r - l) // 2
        if valid(mid, allowed):
            l = mid + 1
            res = mid
        else:
            r = mid - 1
    print(res)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
