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


def atmost(nums, k, _max):
    left = 0
    seen = defaultdict(int)
    ans = 0
    n = len(nums)
    for right in range(n):
        seen[nums[right] ^ big] += 1
        while len(seen) > k:
            seen[nums[left] ^ big] -= 1
            if seen[nums[left] ^ big] == 0:
                del seen[nums[left] ^ big]
            left += 1
        ans += min(right - left + 1, _max)
    return ans


def solve():
    n, k, l, r = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cand1 = atmost(nums, k, r) - atmost(nums, k, l - 1)
    cand2 = atmost(nums, k - 1, r) - atmost(nums, k - 1, l - 1)
    print(cand1 - cand2)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
