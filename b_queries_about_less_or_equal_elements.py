import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    q = list(map(int, input().split()))
    nums.sort()
    ans = []
    for x in q:
        ans.append(bisect_right(nums, x))
    print(*ans)
            


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
