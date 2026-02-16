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
    i = 0
    while i < n - 2:
        if nums[i] < 0:
            print("NO")
            return
        nums[i + 1] -= 2 * nums[i]
        nums[i + 2] -= nums[i]
        nums[i] = 0
        i += 1
    while i < n:
        if nums[i] != 0:
            print("NO")
            return
        i += 1
    print("YES")
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
