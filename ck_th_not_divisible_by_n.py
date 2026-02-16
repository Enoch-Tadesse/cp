import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , k = list(map(int, input().split()))
    if k < n:
        print(k)
        return
    step = n - 1
    temp = (k // step)
    rem = (k % step)
    cand = temp * n + rem
    if cand % n == 0:
        print(cand - 1)
    else:
        print(cand)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
