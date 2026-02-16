import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, s = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    counts = defaultdict(int)
    for num in nums:
        if num % s == 0:
            continue
        else:
            if num > s:
                how = num // s + 1
                counts[(s * how) - num] += 1
            else:
                counts[s- num] += 1
    ans = 0
    for k, v in counts.items():
        ans = max(ans, s * (v - 1) + (k + 1))
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
