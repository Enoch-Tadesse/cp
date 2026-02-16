import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math
from random import *

# input = input
input = sys.stdin.readline


big = randint(1000, 10 ** 6)

def solve():
    nums = list(int(x) for x in input().strip())
    dp = [False] * 9
    dp[0] = True

    for num in nums:
        op = [num]
        if num in [2, 3]:
            op.append(num * num)
        new_dp = [False] * 9
        for r in range(9):
            if not dp[r]:
                continue
            for o in op:
                new_dp[(o + r) % 9] = True
        dp = new_dp
    print("YES" if dp[0] else "NO")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
