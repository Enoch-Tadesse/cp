import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    idx = 0
    counter = 0
    while counter < n:
        if idx % 10 == 3 or idx % 3 == 0:
            idx += 1
            continue
        idx += 1
        counter += 1
    print(idx - 1)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
