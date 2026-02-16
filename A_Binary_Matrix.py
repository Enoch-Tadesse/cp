import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    r, c = list(map(int, input().split()))
    nums = [[int(x) for x in input().strip()] for _ in range(r)]
    r_count = c_count = 0
    for nr in range(r):
        temp = 0
        for nc in range(c):
            temp ^= nums[nr][nc]
        r_count += temp
    for nc in range(c):
        temp = 0
        for nr in range(r):
            temp ^= nums[nr][nc]
        c_count += temp
    print(max(r_count, c_count))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
