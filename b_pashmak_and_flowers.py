import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    _max = max(nums)
    _min = min(nums)
    _max_c = nums.count(_max)
    _min_c = nums.count(_min)
    if _min == _max:
        print(0, (_max_c * (_max_c - 1)// 2))
    else:
        print(_max - _min, (_max_c * _min_c))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
