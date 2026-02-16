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
    pos = -1
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            if pos == -1:
                pos = i
            else:
                print(-1)
                return
    if pos == -1:
        print(0)
    else:
        nums = nums[pos:] + nums[:pos]
        if sorted(nums) == nums:
            print(n - pos )
        else:
            print(-1)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
