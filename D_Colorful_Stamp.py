import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    colors = input().strip().split("W")
    for color in colors:
        if color == "":
            continue
        check = len(color) - color.count("B")
        if check == 0 or check == len(color):
            print("NO")
            return
    print("YES")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
