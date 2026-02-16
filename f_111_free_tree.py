import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , q = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    colors = {i + 1: num for i , num in enumerate(nums)}
    costs = dict()
    for _ in range(n - 1):
        v, u , c = list(map(int, input().split()))
        costs[v][u] = c
        costs[c][v] = c
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
