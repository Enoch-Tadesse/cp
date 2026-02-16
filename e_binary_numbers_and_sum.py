import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

mod =  998244353

def solve():
    n , m = list(map(int, input().split()))
    a = int(input().strip(), 2)
    b = int(input().strip(), 2)
    ans = 0
    while b > 0:
        ans = (ans + (a & b)) % mod
        b >>= 1
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
