import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    total = sum(nums)
    avg = total // 3
    if avg * 3 != total:
        print(0)
        return
    cand = []
    l , curr = 0 , 0
    for r in range(n):
        curr += nums[r]
        if nums[r] == 0:



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
