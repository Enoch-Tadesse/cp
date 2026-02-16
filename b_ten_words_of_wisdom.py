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
    ans, _max = -1, -1
    for i in range(n):
        a, b = list(map(int, input().split()))
        if a > 10:
            continue
        if b > _max:
            _max = b
            ans = i + 1
    print(ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
