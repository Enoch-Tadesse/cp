import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    k , r = list(map(int, input().split()))
    counter = 1
    b = k
    while b % 10 != r and b % 10 != 0:
        b += k
        counter += 1
    print(counter)

def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
