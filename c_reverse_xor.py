import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def isSym(nums):
    l , r = 0 , len(nums) - 1
    while l <= r:
        if nums[l] == nums[r]:
            l , r = l + 1, r - 1
            continue
        return False
    if len(nums) & 1 and nums[len(nums) // 2] == "1":
        return False
    return True
def solve():
    n = int(input())
    nums = list(bin(n))[2:][::-1]
    if "1" not in nums or isSym(nums):
        print("YES")
        return
    iter = nums.index("1")
    for _ in range(iter):
        nums.append("0")
        if isSym(nums):
            print("YES")
            return
    print("NO")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
