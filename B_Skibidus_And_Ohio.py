import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    string = input().strip()

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            print(1)
            return
    print(len(string))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
