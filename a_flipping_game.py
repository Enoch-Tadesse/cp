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
    ones = nums.count(1)
    _max = 0
    for i in range(n):
        for j in range(i, n):
            some = nums[i:j+1]
            zeros = some.count(0)
            o = some.count(1)
            total = ones - o + zeros
            _max = max(_max , total)
    print(_max)


def main():
    t = 1
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
