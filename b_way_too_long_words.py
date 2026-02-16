import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    words = list(x for x in input().strip())
    if (len(words)) > 10:
        print(words[0], end="")
        print(len(words) - 2, end="")
        print(words[-1], end="")
        print()
    else:
        print("".join(words))


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
