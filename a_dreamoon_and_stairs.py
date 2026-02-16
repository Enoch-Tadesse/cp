import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , m = list(map(int, input().split()))
    if m > n:
        print(-1)
    else:
        div = math.ceil(n / 2)
        print(math.ceil(div / m) * m)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
