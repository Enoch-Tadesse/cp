import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    suf = [0] * n
    uni = set()
    for i in range(n - 1, -1, -1):
        uni.add(nums[i])
        suf[i] = len(uni)
    for _ in range(m):
        print(suf[int(input()) - 1])
        


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
