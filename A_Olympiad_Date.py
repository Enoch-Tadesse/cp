import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    need = dict({
        0: 3,
        1: 1,
        3: 1,
        2: 2,
        5: 1,
    })
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        if nums[i] in need:
            need[nums[i]] -= 1
            if need[nums[i]] == 0:
                del need[nums[i]]
        if len(need) == 0:
            print(i + 1)
            return
    print(0)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
