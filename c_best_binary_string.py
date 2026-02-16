import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    nums = list(x for x in input().strip())
    if nums[0] == "?":
        nums[0] = "0"
    if nums[-1] == "?":
        nums[-1] = "1"
    for i in range(1, len(nums) - 1):
        if nums[i] != "?":
            continue
        if nums[i - 1] == "1" or nums[i + 1] == "1":
            nums[i] = "1"
        else:
            nums[i] = "0"
    print("".join(nums))




def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
