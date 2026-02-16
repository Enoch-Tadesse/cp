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
    if n == 1:
        print(0)
        return
    _min  = min(nums[0] , nums[1])
    _max = max(nums[0] , nums[1])
    counter = 1 * int(_min != _max)
    for i in range(2, n):
        if nums[i] > _max:
            counter += 1
            _max = nums[i]
        if nums[i] < _min:
            counter += 1
            _min = nums[i]
    print(counter)



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
