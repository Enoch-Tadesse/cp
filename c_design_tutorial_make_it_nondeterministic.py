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
    names = []
    for _ in range(n):
        a, b = list(map(str, input().split()))
        if a > b:
            a, b = b, a
        names.append((a, b))
    p = list(map(int, input().split()))
    curr = -1
    for ele in p:
        ele -= 1
        if curr == -1:
            curr = names[ele][0]
            continue
        if names[ele][0] >= curr:
            curr = names[ele][0]
        elif names[ele][1] >= curr:
            curr = names[ele][1]
        else:
            print("NO")
            return
    print("YES")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
