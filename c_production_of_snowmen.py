import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    first = [[True] * n for _ in range(n)]
    second = [[True] * n for _ in range(n)]

    for d in range(n):
        bad = 0
        for t in range(n):
            if a[t] >= b[(t + d) % n]:
                bad += 1
        for i in range(n):
            j = (i + d) % n
            if bad > 0:
                first[i][j] = False
            if a[i] >= b[(i + d) % n]:
                bad -= 1
            if a[(i + n) % n] >= b[(i + d + n) % n]:
                bad += 1

    for d in range(n):
        bad = 0
        for t in range(n):
            if b[t] >= c[(t + d) % n]:
                bad += 1
        for j in range(n):
            k = (j + d) % n
            if bad > 0:
                second[j][k] = False
            if b[j] >= c[(j + d) % n]:
                bad -= 1
            if b[(j + n) % n] >= c[(j + d + n) % n]:
                bad += 1

    ans = 0
    for j in range(n):
        cnt_i = sum(first[i][j] for i in range(n))
        cnt_k = sum(second[j][k] for k in range(n))
        ans += cnt_i * cnt_k

    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
