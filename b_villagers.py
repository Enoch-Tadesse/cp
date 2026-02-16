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
    nums.sort(reverse=True)
    counter = 0
    i = 0
    while i < n -1:
        counter += max(nums[i] , nums[i + 1])
        i += 2
    if n & 1:
        counter += nums[-1]
    print(counter)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
