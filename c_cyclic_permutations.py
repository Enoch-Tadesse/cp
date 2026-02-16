import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

mod = 10**9 + 7

def solve():
    n = int(input())
    
    # Compute factorial n! % mod
    fac = 1
    for i in range(2, n + 1):
        fac = (fac * i) % mod
    
    # Compute 2^(n-1) % mod
    pow2 = pow(2, n-1, mod)
    
    ans = (fac - pow2 + mod) % mod  # add mod to avoid negative
    print(ans)
 

def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
