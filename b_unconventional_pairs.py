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
    nums = list(sorted(list(map(int, input().split()))))
    ans = float("-inf")
    for i in range(0, len(nums), 2):
        ans = max(nums[i + 1] - nums[i], ans)
    print(ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
