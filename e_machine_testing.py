import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def can(time, h, p):
    n = len(h)
    damage = time * p[0]
    for i in range(1, n):
        if h[i] > damage:
            return False
        time -= 1
        if time < 0:
            return False
        damage += p[i]
    return True





def solve():
    n = int(input())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))
    l , r = 0 , max(h) + 1
    while l <= r:
        mid = l + (r - l) // 2
        if can(mid, h, p):
            r = mid - 1
        else:
            l = mid + 1
    print(l)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
