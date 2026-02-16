import sys

sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, m, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    par = {i: i for i in range(1, n + 1)}

    def find(node):
        if par[node] != node:
            par[node] = find(par[node])
        return par[node]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            par[rx] = ry
        return True

    for _ in range(m):
        a, b = list(map(int, input().split()))
        union(a, b)

    # for each unions, how many has what color
    group = defaultdict(list)
    for i in range(1, n + 1):
        group[find(i)].append(i)
    ans = 0
    for k , v in group.items():
        eles = v
        cnts = defaultdict(int)
        for e in eles:
            cnts[nums[e - 1]] += 1
        _max = max(cnts.values())
        ans += sum(cnts.values()) - _max
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
