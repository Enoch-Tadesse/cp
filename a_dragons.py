import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    s , n = list(map(int, input().split()))
    
    nums = []
    for _ in range(n):
        nums.append(tuple(list(map(int, input().split()))))
    nums.sort()
    for x , y in nums:
        if s < x:
            print("NO")
            return
        s += y
    print("YES")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
