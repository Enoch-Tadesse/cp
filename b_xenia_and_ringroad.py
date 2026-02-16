import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    time = 0
    i = 0
    isIn = 1
    while i < k:
        if nums[i] == isIn:
            i += 1
            continue
        if nums[i] > isIn:
            time += nums[i] - isIn
        else:
            time += nums[i] + n - isIn
        isIn = nums[i]
    print(time)


def main():
    t = 1
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
