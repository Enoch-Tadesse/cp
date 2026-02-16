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
    total = sum(nums)
    counts = Counter(nums) # count of each number in nums
    arr = list(counts.keys())
    _max = max(arr)
    _min = min(arr)

    if counts[_max] > 1:
        if _max - _min > k:
            print("Jerry")
            return
    if _max - _min - 1 > k:
        print("Jerry")
        return
    if total & 1 == 0:
        print("Jerry")
        return
    print("Tom")
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
