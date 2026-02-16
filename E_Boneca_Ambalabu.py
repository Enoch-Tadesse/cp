import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    cand = set()
    bits = [0] * 32
    for i in range(31, -1, -1):
        for num in nums:
            bits[i] += (num >> i) & 1
    res = 0
    for num in nums:
        counter = 0
        for i in range(31, -1, -1):
            if (num >> i) & 1:
                zeros = n - bits[i]
                counter += zeros * (1 << i)
            else:
                ones = bits[i]
                counter += ones * (1 << i)
        res = max(res, counter)
    print(res)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
