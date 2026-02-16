import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = input


def solve():
    num = int(input())
    if num % 2 == 1:
        print((num - 1) // 2 - num)
    else:
        print(num // 2)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
