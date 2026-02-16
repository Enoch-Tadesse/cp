import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    a = input().strip()
    b = input().strip()
    # for i in range(len(r1)):
    #     a , b = r1[i].lower(), r2[i].lower()
    a = a.lower()
    b = b.lower()
    if (a < b) :
        print("-1")
        return
    elif (a > b) :
        print("1")
        return
    print("0")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
