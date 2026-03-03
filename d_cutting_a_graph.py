import sys
sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def solve():
    n , e, o = list(map(int, input().split()))
    cnts = defaultdict(int)

    for _ in range(e):
        a, b = list(map(int, input().split()))
        if a > b:
            a, b = b , a
        cnts[(a, b)] += 1
    queries = []
    for _ in range(o):
        t, a, b = list(map(str, input().split()))
        a , b = int(a) , int(b)
        if a > b:
            a, b = b , a
        queries.append((t, a, b))
    queries.reverse()

    par = {i : i for i in range(1, n + 1)}

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return 
        par[px] = py


    ans = []
    for t, a , b in queries:
        if t == "ask":
            ans.append("YES" if find(a) == find(b) else "NO")
        else:
            cnts[(a, b)] -= 1
            if cnts[(a, b)] != 0:
                continue
            union(a, b)
    ans.reverse()
    print(*ans, sep="\n")
    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
