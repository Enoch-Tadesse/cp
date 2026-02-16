import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

mod = 998244353

def fac(x):
    ans = 1
    for i in range(1, x + 1):
        ans = (ans * i) % mod
    return ans



def solve():
    nums = list(int(x) for x in input().strip())
    ans, way = 0, 0
    l = 0
    bricks = []
    for r in range(len(nums)):
        if nums[r] == nums[l]:
            continue
        bricks.append(r - l)
        l = r

    n = len(nums)
    if n - l >= 1:
        bricks.append(n - l)

    way = 1
    for num in bricks:
        way = (way * num) % mod

    z = n - len(bricks)
    way = (way * fac(z)) % mod

    ans = n - len(bricks)
    print(*(ans, way % mod))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
