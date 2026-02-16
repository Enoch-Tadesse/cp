import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = input


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    i = counter = 0
    while i < n - 1:
        if nums[i] > nums[i + 1]:
            i += 1
            counter += 1
        i += 1
    print(counter)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
