import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    x, y = list(map(int, input().split()))
    if x == y:
        print(-1)
        return
    last = -1
    ans = 0
    for i in range(32):
        compare = 1 << i
        f = x & compare
        s = y & compare
        if f == s == 0:
            continue
        if f == s:
            if last >= 0:
                for k in range(last, i):
                    add = 1 << k
                    x += add
                    y += add
                    ans += add
            else:
                ans += compare
                x += compare
                y += compare
                continue
        last = i
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
