import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *

# input = input
input = sys.stdin.readline


def solve():
    n, q = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    pre = [0]
    for num in nums:
        pre.append(pre[-1] + num)
    for _ in range(q):
        l, r = list(map(int, input().split()))
        size = r - l + 1
        _sum = pre[r] - pre[l - 1]
        if size & 1:
            print("NO")
        else:
            if _sum & 1:
                print("NO")
            else:
                _max = max(nums[l - 1 : r])
                if 2 * _max > _sum:
                    print("NO")
                else:
                    print("YES")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
