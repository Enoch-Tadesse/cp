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
    s = input().strip()
    t = input().strip()
    p = input().strip()

    i = 0
    j = 0

    need = dict()

    i_have = dict()
    for k in range(len(p)):
        i_have[p[k]] = i_have.get(p[k], 0) + 1


    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        else:
            need[t[j]] = need.get(t[j], 0) + 1
        j += 1

    if i != len(s):
        print("NO")
        return

    while j < len(t):
        need[t[j]] = need.get(t[j], 0) + 1
        j += 1

    for k , v in need.items():
        if k not in i_have or i_have[k] < v:
            print("NO")
            return

    print("YES")



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
