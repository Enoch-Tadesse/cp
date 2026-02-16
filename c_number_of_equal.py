import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *

# input = input
input = sys.stdin.readline


def solve():
    n, m = list(map(int, input().split()))
    top = list(map(int, input().split()))
    bottom = list(map(int, input().split()))

    answer = 0

    i = 0
    j = 0
    while i < n and j < m:
        if top[i] != bottom[j]:
            # move the smaller number to the right
            if top[i] > bottom[j]:
                j += 1
            else:
                i += 1
        else:
            count1, count2 = 0, 0
            number = top[i]  # we could take bottom[j], they are equal
            # count how many numbers are equal to out number from top array
            while i < n and top[i] == number:
                count1 += 1
                i += 1

            # count how many numbers are equal to out number from top array
            while j < m and bottom[j] == number:
                count2 += 1
                j += 1

            # their multiplication should be added to our answer
            answer += count1 * count2
    print(answer)


def main():
    t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
