import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , s , x = list(map(int, input().split()))
    pre = [0] * (n + 1)
    nums = list(map(int, input().split()))
    for i in range(1, n+1):
        pre[i] = pre[i-1] + nums[i- 1]
    counter = 0
    freq = defaultdict(int)
    left = 1
    for right in range(1, n + 1):
        if (nums[right - 1] > x):
            freq.clear()
            left = right + 1
        elif (nums[right - 1] == x):
            while left <= right:
                freq[pre[left - 1]] += 1
                left += 1
        counter += freq[pre[right]- s]
    print(counter)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
