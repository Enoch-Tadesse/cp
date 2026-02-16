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
    nums[0] = min(2 * n - nums[0] , nums[0])
    arr = [nums[0]]
    for i in range(1, n):
        if arr[i-1] > nums[i]:
            arr.append(2 * n - nums[i])
        else:
            arr.append(nums[i])
    counts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                counts += 1 
    print(arr)
    print(counts)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
