import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    dis = list(map(int, input().split()))
    nums.sort(reverse=True)
    dis.sort()
    u = 0
    l = 0
    counter = 0
    while u < n and l < k:
        counter += sum(nums[u : min(u + dis[l] - 1, n)])
        u += dis[l]
        l += 1
    print(counter + sum(nums[u:]))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
