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
    l , r = 0 , n - 1
    curr = 1
    while l <= r:
        if nums[l] == curr:
            l += 1
        elif nums[r] == curr:
            r -= 1
        else:
            print("NO")
            return
        curr += 1
    print("YES")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
