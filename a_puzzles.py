import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , m = list(map(int, input().split()))
    
    nums = list(map(int, input().split()))
    nums.sort()
    ans = float("inf")
    for i in range(n-1, m):
        ans = min(ans, nums[i] - nums[i-n + 1])
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
