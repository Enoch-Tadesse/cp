import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , m , k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    queries = []
    for _ in range(m):
        l , r, d = list(map(int, input().split()))
        l -= 1
        r -= 1
        queries.append((l , r, d))
    pre = [0] * (m + 1)
    for _ in range(k):
        l , r = list(map(int, input().split()))
        l -= 1
        r -= 1
        pre[l] += 1
        pre[r + 1] -= 1
    for i in range(1, len(pre)):
        pre[i] += pre[i - 1]

    delta = [0] * (n + 1)
    for i, p in enumerate(pre):
        if p <= 0:
            continue
        if i >= m:
            continue
        l , r, d = queries[i]
        delta[l] += d * p
        delta[r + 1] -= d * p
    for i in range(1, len(delta)):
        delta[i] += delta[i - 1]
    for i in range(n):
        nums[i] += delta[i]
    print(*nums)

    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
