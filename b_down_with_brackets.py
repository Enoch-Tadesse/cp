import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    brack = list(x for x in input().strip())
    n = len(brack)
    status = 0
    for i in range(1,n - 1):
        if brack[i] == '(':
            status += 1
        else:
            status -= 1
        if status < 0:
            print("YES")
            return
    if status == 0:
        print("NO")
    else:
        print("YES")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
