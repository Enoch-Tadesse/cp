import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def reduce(x):
    while x % 2 == 0:
        x //= 2
    while x % 3 == 0:
        x //= 3
    return x


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    pre = reduce(nums[0])
    for i in range(1, len(nums)):
        if reduce(nums[i]) != pre:
            print("No")
            return
    print("Yes")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
