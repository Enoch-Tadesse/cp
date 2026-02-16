import sys
# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    _min = min(nums)
    _max = max(nums)
    idx1 = nums.index(_min)
    idx2 = nums.index(_max)
    print(max(abs(n - idx2 - 1), abs(n - idx1 - 1), abs(idx2 ), abs(idx1)))



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
