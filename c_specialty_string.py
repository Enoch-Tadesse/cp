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
    n = int(input())
    chars = list(x for x in input().strip())
    stack = []
    for c in chars:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    print("YES" if not stack else "NO")
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
