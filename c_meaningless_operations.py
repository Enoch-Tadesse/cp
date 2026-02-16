import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    ans = []
    for i in range(n.bit_length()):
        ans.append(int(n & (1 << i) == 0))
    if sum(ans) == 0:
        curr = 0
        curr = max(curr, math.gcd(n ^ 1, n & 1))
        for i in range(2, math.ceil(math.sqrt(n))):
            if n % i == 0:
                cand = math.gcd(n ^ i, n & i)
                idx = n // i
                cand2 = math.gcd(n ^ idx, n & idx)
                curr = max(curr, cand2, cand)
        print(curr)

    else:
        b = 0
        for i in range(len(ans)):
            b <<= 1
            b ^= ans.pop()
        print(b ^ n)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
