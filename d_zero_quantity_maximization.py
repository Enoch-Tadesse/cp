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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    div = defaultdict(int)
    count = 0
    for i in range(n):
        if a[i] == 0 or b[i] == 0:
            if a[i] == 0 and b[i] == 0:
                count += 1
            elif b[i] == 0:
                div[(0 , 1)] += 1
        else:
            num , den = -b[i] , a[i]
            gcd = math.gcd(num , den)
            num //= gcd
            den //= gcd
            if den < 0:
                num *= -1
                den *= -1
            div[(num , den)] += 1
    if len(div) == 0:
        print(0 + count)
    else:
        print(max([v for _ , v in div.items()]) + count)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
