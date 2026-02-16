import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def bubble_sort(nums, code):
    n = len(nums)
    swaps = []
    for i in range(n):
        for j in range(n - 1-i):
            if nums[j] > nums[j + 1]:
                swaps.append((code, j + 1))
                nums[j] , nums[j + 1] = nums[j + 1] , nums[j]

    return swaps

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    swaps = bubble_sort(a, 1)
    swaps.extend(bubble_sort(b, 2))

    for i in range(n):
        if a[i] > b[i]:
            a[i] , b[i] = b[i], a[i]
            swaps.append((3, i + 1))
    print(len(swaps))
    for x , y in swaps:
        print(x, y )
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
