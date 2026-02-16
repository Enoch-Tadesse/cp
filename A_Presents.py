import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = input


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = [0] * n
    for i, num in enumerate(nums):
        ans[num - 1] = i + 1
    print(*ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
