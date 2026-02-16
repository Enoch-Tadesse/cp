import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    chars = list(x for x in input().strip())
    i = 0
    n = len(chars)

    while i < n:
        if chars[i] == "a":
            i += 1
            continue
        break
    z = i + 1
    if i == n:
        print("".join(chars))
        return
    while z < n:
        if chars[z] == "a":
            break
        z += 1
    for j in range(i, z):
        c = chars[j]
        y = (ord(c) - ord("a") - 1) % 26
        chars[j] = chr(ord("a") + y)
    print("".join(chars))


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
