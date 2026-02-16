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
    sig = list(map(int, input().split()))
    pre = [0]
    for i, num in enumerate(nums):
        pre.append(num * sig[i] + pre[-1])
    suf = [0]
    for i, num in enumerate(nums[::-1]):
        j = n - i - 1
        suf.append(num * sig[j] + suf[-1])
    suf = suf[::-1]
    l = 0
    counter = 0
    ans = 0
    for r in range(n):
        if r - l + 1 < k:
            counter += nums[r]
            continue
        counter += nums[r]
        ans = max(ans, counter + pre[l] + suf[r + 1])
        counter -= nums[l]
        l += 1
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
