import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    k, x = list(map(int, input().split()))

    l, r = 1, k
    while l <= r:
        mid = (l + r) // 2
        can = (mid) * (mid + 1) // 2
        if can <= x:
            l = mid + 1
        else:
            r = mid - 1
    ans = r
    total = (r ) * (r + 1) // 2
    if (x - total <= 0) :
        print(ans)
        return

    x -= total
    l , r = 1, k - 1

    while l <= r:
        mid = (l + r) // 2
        can = (mid) * (mid + 1) // 2
        if can <= x:
            l = mid + 1
        else:
            r = mid - 1
    # while l >= r:
    #     mid = (l + r) // 2
    #     can = (l + mid) * (l - mid + 1) // 2
    #     print(can)
    #     if can <= x:
    #         l = mid + 1
    #     else:
    #         r = mid - 1
    print(ans + r)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
