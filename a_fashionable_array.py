import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    counts = Counter(nums)
    arr = list(counts.keys())
    arr.sort()
    if (arr[0] & 1 == arr[-1]& 1):
        print(0)
        return
    count1 = 0
    l = 0
    while (l < len(arr) and arr[0] & 1 == arr[l] & 1):
        count1 += counts[arr[l]]
        l += 1
    count2 = 0
    r = len(arr) - 1 
    while (r > -1 and arr[-1] & 1 == arr[r] & 1):
        count2 += counts[arr[r]]
        r -= 1 
    print(min(count1, count2))


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
