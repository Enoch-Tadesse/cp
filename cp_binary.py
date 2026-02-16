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
    k = 1
    while True:
        target = n - (m * k)
        if k > target:
            print("-1")
            return
        if k >= target.bit_count():
            print(k)
            return
        k += 1



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
