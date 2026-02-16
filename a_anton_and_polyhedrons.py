from contextlib import redirect_stderr
import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    values = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20,
    }
    counter = 0
    for _ in range(n):
        counter += values[input().strip()]
    print(counter)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
