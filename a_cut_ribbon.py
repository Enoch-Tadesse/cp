import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, a, b, c = list(map(int, input().split()))
    ans = 0
    for x in range(n + 1):
        for y in range(n + 1):
            curr = n - (x * a + y * b)
            if curr < 0:
                continue
            if curr % c == 0:
                ans = max(curr//c + x + y, ans)
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
