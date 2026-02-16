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
    non_delete = set()
    curr_unique = set()
    next_unique = set()
    for k , v in counts.items():
        if v == 1:
            curr_unique.add(k)
    idx = n - 1
    counter = 0
    while idx > -1:
        x = counts[nums[idx]]
        if nums[idx] not in non_delete:
            counts[nums[idx]] -= 1
            if x == 2:
                next_unique.add(nums[idx])
            if x == 1:
                del counts[nums[idx]]
                curr_unique.discard(nums[idx])
            else:
                non_delete.add(nums[idx])
            idx -= 1
        else:
            if len(curr_unique) > 0:
                break
            curr_unique = next_unique
            next_unique = set()
            counter += 1
            non_delete.clear()
    print(counter + 1)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
