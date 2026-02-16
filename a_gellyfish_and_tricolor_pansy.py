import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    a , b , c , d = list(map(int, input().split()))
    f = min(b , d)
    g = min(a, c)
    if g >= f:
        print("Gellyfish")
    else:
        print("Flower")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
