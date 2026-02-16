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
    target = 1
    for num in nums:
        target = math.lcm(target, num)
    cand = 1
    for i in range(n-2, -1, -1):
        if nums[i + 1] % nums[i] != 0:
            _min = min(nums[i + 1], nums[i])
            cand = max(cand, _min // math.gcd(nums[i], nums[i + 1]))
    print(cand)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
