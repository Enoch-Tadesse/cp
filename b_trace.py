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
    nums.sort(reverse=True)
    count = 0
    for i in range(n):
        val = nums[i] * nums[i]
        if i & 1:
            count -= val
        else:
            count += val
    print(count * math.pi)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
