import sys
#sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import math

# input = input
input = sys.stdin.readline

def alt(og):
    nums = []
    for num in og:
        if num <= 0:
            continue
        nums.append(num)
    if not nums:
        return 1
    _min = min(nums)
    nums = set([num - _min for num in nums])
    nums = sorted(list(nums))
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)
    

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    x = alt(nums[:])
    _min = min(nums)
    nums = set([num - _min for num in nums])
    nums = sorted(list(nums))
    y = len(nums)
    for i in range(len(nums)):
        if nums[i] != i:
            y = i
            break
    print(max(y , x))



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
