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
    l , r = 1 , n - 2
    while l < r:
        if nums[l] == nums[l - 1] or nums[r] == nums[r + 1]:
            nums[l] , nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    ans = 0
    for i in range(n - 1):
        ans += int(nums[i] == nums[i + 1])
    print(ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
