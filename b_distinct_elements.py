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
    curr = 1
    pre = 0
    ans = [0] * n
    for i in range(n):
        diff = pre - nums[i] + i + 1
        if diff == 0:
            ans[i] = curr
            curr += 1
        else:
            ans[i] = ans[diff - 1]
        pre = nums[i]
    print(*ans)
            


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
