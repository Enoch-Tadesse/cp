import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def calc(nums):
    ans = 0
    total = 0
    for num in nums:
        total += num
        ans = max(ans, total)
    return ans

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    print(calc(nums) + calc(nums2))


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
