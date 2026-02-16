import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

sys.setrecursionlimit(1 << 25)

input = sys.stdin.readline

way = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def traverse(grid, checker, r, c, visited):
    if grid[r][c] == "?":
        return False
    if (r, c) in visited:
        return checker[r][c]
    visited.add((r, c))
    nr, nc = way[grid[r][c]]
    r, c = r + nr, c + nc
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        checker[r - nr][c - nc] = True
        return True
    val = traverse(grid, checker, r, c, visited)
    checker[r - nr][c - nc] = val
    return val


def solve():
    r, c = list(map(int, input().split()))
    visited = set()
    grid = [[x for x in input().strip()] for _ in range(r)]
    checker = [
        [False] * c for _ in range(r)
    ]  # this does a dfs and find places where we can extrap then
    for nr in range(r):
        for nc in range(c):
            if (nr, nc) in visited:
                continue
            val = traverse(grid, checker, nr, nc, visited)
            checker[nr][nc] = val

    counter = 0
    for nr in range(r):
        for nc in range(c):
            if grid[nr][nc] != "?":
                if not (checker[nr][nc]):
                    counter += 1
                continue
            status = True
            for dr, dc in [
                (-1 + nr, nc),
                (1 + nr, nc),
                (nr, nc - 1),
                (nr, nc + 1),
            ]:
                if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]):
                    status &= checker[dr][dc]
            counter += not (status)
    print(counter)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    import threading

    threading.Thread(target=main).start()
    # main()
