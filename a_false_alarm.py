import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    l = 0
    for i in range(n):
        if nums[i] == 1:
            l = i
            break
    r = n - 1
    for i in range(n-1, -1, -1):
        if nums[i] == 1:
            r = i
            break
    dist = r - l + 1 
    print("YES" if dist <= k else "NO")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
