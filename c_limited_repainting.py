import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def checker(colors, pens, guess, k, bees):
    # check if bees is one
    if len(bees) == 1:
        k -= pens[bees[0]] > guess
    else:
        for i in range(1, len(bees)):
            check = pens[bees[i - 1] + 1 : bees[i]]
            check.append(0)
            if max(check) > guess:
                k -= 1
                if i == len(bees):
                    k -= 1
    return k >= 1


def solve():
    n, k = list(map(int, input().split()))
    colors = list(x for x in input().strip())
    bees = [i for i in range(n) if colors[i] == "B"]
    pens = list(map(int, input().split()))
    l = 0
    r = max(pens)
    while l <= r:
        mid = l + (r - l) // 2
        if checker(colors, pens, mid, k, bees):
            r = mid - 1
        else:
            l = mid + 1
    print(l)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
