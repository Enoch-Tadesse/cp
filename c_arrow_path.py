import sys

# sys.setrecursionlimit(10**9)
from collections import Counter, defaultdict, deque
from functools import lru_cache
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    mat = [list(input().strip()) for _ in range(2)]

    from collections import deque

    q = deque()
    visited = set()

    q.append((0, 0, 0))
    visited.add((0, 0, 0))
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while q:
        r, c, s = q.popleft()

        if r == 1 and c == n - 1:
            print("YES")
            return

        if s == 0:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 2 and 0 <= nc < n:
                    if (nr, nc, 1) not in visited:
                        visited.add((nr, nc, 1))
                        q.append((nr, nc, 1))
        else:
            if mat[r][c] == ">":
                nc = c + 1
                if 0 <= nc < n and (r, nc, 0) not in visited:
                    visited.add((r, nc, 0))
                    q.append((r, nc, 0))
            else:
                nc = c - 1
                if 0 <= nc < n and (r, nc, 0) not in visited:
                    visited.add((r, nc, 0))
                    q.append((r, nc, 0))

    print("NO")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
