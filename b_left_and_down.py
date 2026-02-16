import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    a , b , k = list(map(int, input().split()))
    if k >= a and k >= b:
        print(1)
    else:
        gcd = math.gcd(a, b)
        if gcd == 1:
            print(2)
            return
        if a / gcd <= k and b / gcd <= k:
            print(1)
        else:
            print(2)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
