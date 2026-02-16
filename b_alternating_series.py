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
    neg = True
    for _ in range(n):
        if neg:
            ans.append(-1)
            neg = False
        else:
            ans.append(3)
            neg = True
    if n & 1:
        pass
    else:
        ans[-1] = 2
    print(*ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
