import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def valid(nums, l):
    if nums[l] + 1 <= nums[l + 1] and nums[l + 1] + 1 <= nums[l + 2]:
        return True
    return False

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    counter = 1
    i = 0
    for i in range(n-2):
        if nums[i] + 1 <= nums[i + 1] and nums[i + 1] + 1 <= nums[i + 2]:
            continue
        counter += 1
    print(counter)
    while i < n - 2 and counter > 0:
        if valid(nums, i):
            counter -= 1
            i += 1
        i += 1
    print(counter)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
