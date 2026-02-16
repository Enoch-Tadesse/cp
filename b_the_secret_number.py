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
    ans = []
    for i in range(1, 18):
        p = 10 ** i
        if n % (p + 1) == 0:
            ans.append(n // (p + 1))
    print(len(ans))
    ans.sort()
    if len(ans) > 0:
        print(*ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
