import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    ans = math.comb(n, 5) + math.comb(n , 6) + math.comb(n,  7)
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
