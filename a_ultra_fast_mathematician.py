import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = input().strip()
    m = input().strip()
    ans = []
    for i in range(len(n)):
        if n[i] != m[i]:
            ans.append("1")
        else:
            ans.append("0")
    print("".join(ans))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
