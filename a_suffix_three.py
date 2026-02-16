import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    w = input().strip()
    if w[-1] == "o":
        print("FILIPINO")

    elif w[-1] == "u":
        print("JAPANESE")

    else:
        print("KOREAN")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
