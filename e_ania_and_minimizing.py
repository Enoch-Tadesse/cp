import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    nums = list(str(x) for x in input().strip())
    if k == 0:
        print( "".join(nums))
        return
    if (len(nums)) == 1:
        print("0")
        return
    if nums[0] != "1":
        k -= 1
        nums[0] = "1"
    i = 1
    while i < len(nums) and k > 0:
        if nums[i] != "0":
            nums[i] = "0"
            k -= 1
        i += 1
    print("".join(nums))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
