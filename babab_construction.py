from functools import lru_cache
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

chars = []
og = []

@lru_cache
def can(l, r, curr):
    if (l > r): return True
    need = og[curr]





def solve():
    global chars
    global og
    n = int(input())
    chars = list(x for x in input().strip())
    og = ['a' if i & 1 else 'b' for i in range(1, n + 1)]
    # print(chars, og)
    # print(chars)
    # init = 'a' if n & 1 else 'b'
    # print("YES" if can(0, n - 1, init) else "NO")
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
