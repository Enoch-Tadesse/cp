import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def log(grid):
    for row in grid:
        print("".join(row))


def solve():
    n, k = list(map(int, input().split()))
    grid = [["D"] * n for _ in range(n)]
    k = n * n - k
    if k == 1:
        print("NO")
        return
    for i in range(n):
        for j in range(n):
            if k > 0:
                if i == 0 and j == 0:
                    grid[i][j] = "R"
                elif i == 0:
                    grid[i][j] = "L"
                else:
                    grid[i][j] = "U"
            k -= 1
    print("YES")
    log(grid)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
