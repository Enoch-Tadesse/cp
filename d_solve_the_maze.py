import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def solve():
    rows, cols = list(map(int, input().split()))
    mat = [list(x for x in input().strip()) for _ in range(rows)]
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    goods, bads = 0, 0
    q = deque([])
    for r in range(rows):
        for c in range(cols):
            goods += mat[r][c] == "G"
            if mat[r][c] == "B":
                bads += 1
                q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if 0 <= nr < rows and 0 <= nc < cols:
                if mat[nr][nc] == ".":
                    mat[nr][nc] = "#"
    if not goods:
        print("YES")
        return
    if mat[rows - 1][cols - 1] == "#":
        print("NO")
        return
    q = deque([(rows - 1, cols - 1)])
    mat[rows - 1][cols - 1] = "#"
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if mat[nr][nc] == "B":
                    print("NO")
                    return
                if mat[nr][nc] != "#":
                    goods -= mat[nr][nc] == "G"
                    mat[nr][nc] = "#"
                    q.append((nr, nc))
    print("YES" if not goods else "NO")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
