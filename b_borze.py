import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    chars = input().strip()
    dash = False
    ans = []
    for i, c in enumerate(chars):
        if c == ".":
            if dash:
                ans.append("1")
                dash = False
            else:
                ans.append("0")
        else:
            if dash:
                ans.append("2")
                dash = False
            else:
                dash = True
    print("".join(ans))


def main():
    t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
