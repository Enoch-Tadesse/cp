import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , m , a , b = list(map(int, input().split()))
    counter = 1
    n = a
    while n != 1 or m != 1:
        if (n > 1):
            counter += 1
            n //= 2
        elif (m > 1):
            counter += 1
            m //= 2
    
    print(counter)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
