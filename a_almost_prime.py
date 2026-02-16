import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

_max = 3001
fac = [0] * _max
for i in range(2, _max):
    if fac[i] == 0:
        for j in range(i, _max, i):
            if fac[j] == 0:
                fac[j] = i

def isAlmost(num):
    factors = set()
    while num > 1:
        factors.add(fac[num])
        num //= fac[num]
    return len(factors) == 2
    

def solve():
    n = int(input())
    almost = 0
    for i in range(1, n + 1):
        almost += isAlmost(i)
    print(almost)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
