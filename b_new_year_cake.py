import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    a, b = map(int, input().split())

    odd = 0
    even = 0
    size = 1
    ans = 0

    for layer in range(1, 30):
        if layer % 2 == 1:
            odd += size
        else:
            even += size

        if (odd <= a and even <= b) or (odd <= b and even <= a):
            ans = layer
        else:
            print(ans)
            return

        size <<= 1

    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
