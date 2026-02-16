import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def strict(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            return False
    return True


def solve():
    n , m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    if strict(nums):
        print(n - nums[-1] + 1)
        return
    print(1)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
