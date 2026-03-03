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
    ones = chars.count("1")
    zeros = n - ones
    if ones & 1:


        print(-1)
        return
    print(ones)
    print(*[i + 1 for i in range(n) if chars[i] == "1"])

    # 111000
    # 000011

    # 0001
    # 1111
    # 1000
    # 0011
    # 1110
    # 0000

    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
