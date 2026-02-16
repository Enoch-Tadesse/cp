import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import math

# input = input
input = sys.stdin.readline

big = randint(1, 1 << 9)


def solve():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    counts = Counter(nums)
    ans = counts[k]
    below = 0
    for num in counts.keys():
        below += num < k
    print(max(ans, k - below))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
