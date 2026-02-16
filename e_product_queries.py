import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    cnts = defaultdict(int)

    dp = [float("inf")] * (n + 1)
    for num in nums:
        cnts[num] += 1
        dp[num] = 1

    ans = []
    for i in range(1, n + 1):
        if dp[i] == float("inf"):
            ans.append(-1)
            continue
        else:
            for j in range(i + i, n + 1, i):
                x = j // i
                if cnts[x]:
                    dp[j] = min(dp[j], dp[i] + 1)
        ans.append(dp[i])
    print(*ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
