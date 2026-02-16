import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(int(x) for x in input().strip())

    curr = 0
    counter = 0
    turns = 0
    for i in range(n):
        if nums[i] == curr:
            counter += 1
        else:
            curr = 1 - curr
            turns += 1
            counter += 2
    if turns < 2:
        print(counter)
    elif turns == 2:
        print(counter - 1)
    else:
        print(counter - 2)
    # print(f"{counter=} {turns=}")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
