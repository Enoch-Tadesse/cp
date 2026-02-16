import sys
# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    chars = list(x for x in input().strip())
    stack = []
    for c in chars:
        if c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                continue
        stack.append(c)
    print(len(stack) // 2)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
