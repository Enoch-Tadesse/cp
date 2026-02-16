import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    shops = list(map(int, input().split()))
    shops.sort()
    t = int(input())
    for _ in range(t):
        k = int(input())
        print(bisect_right(shops, k))
    return


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
