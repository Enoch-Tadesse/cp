import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    if n >= 1900:
        print("Division 1")
    elif n >= 1600:
        print("Division 2")
    elif n >= 1400:
        print("Division 3")
    else:
        print("Division 4")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
