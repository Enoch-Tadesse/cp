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
    ans = []
    l , r = 0 , n - 1
    while l <= r:
        ans.append(nums[l])
        ans.append(nums[r])
        l += 1
        r -= 1
    if n & 1:
        ans.pop()
    print(*ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
