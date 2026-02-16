import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, x = list(map(int, input().split()))
    if n * n < x:
        print(0)
        return
    go = math.ceil(math.sqrt(x))
    counter = 0
    for i in range(1, go):
        if x % i == 0:
            a, b = i, x // i
            if a <= n and b <= n:
                counter += 1
    counter *= 2
    if x == go * go:
        counter += 1
    print(counter)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
