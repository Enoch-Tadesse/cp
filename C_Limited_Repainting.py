import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def valid(guess, pens, string, k):
    counter = 0  # counts how many operations needed for this guess
    i = 0
    while i < len(string):
        while i < len(string) and not (string[i] == "R" and pens[i] > guess):
            i += 1
        counter += 1
        i += 1
    return counter <= k  # counter should be under allowed operations


def solve():
    n, k = list(map(int, input().split()))
    string = input().strip()
    pens = list(map(int, input().split()))
    left, right = 0, max(pens)
    while left <= right:
        mid = left + (right - left) // 2
        if valid(mid, pens, string, k):
            right = mid - 1
        else:
            left = mid + 1
    print(left)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
