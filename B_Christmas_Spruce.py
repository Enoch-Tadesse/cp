import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    adj = defaultdict(list)
    for i in range(n - 1):
        adj[int(input())].append(i + 2)
    for parent in adj.keys():
        leafs = 0
        for value in adj[parent]:
            if value not in adj:
                leafs += 1
        if leafs < 3:
            print("No")
            return

    print("Yes")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
