import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())

    a = input().strip()
    b = input().strip()
    acount, bcount = 0, 0
    for i in range(n):
        if i & 1:
            acount += int(a[i] == "0")
            bcount += int(b[i] == "0")
        else:
            acount += int(b[i] == "0")
            bcount += int(a[i] == "0")
    if acount >= (n) // 2 and bcount >= (n + 1) // 2:
        print("YES")
    else:
        print("NO")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
