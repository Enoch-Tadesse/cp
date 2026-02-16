import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    seen = set()
    seen.add(0)
    pref = 0
    ans = 0

    for num in nums:
        prev = pref
        pref += num
        if pref in seen:
            ans += 1
            # seen.clear()
            seen = {prev}
        seen.add(pref)
    print(ans)



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
