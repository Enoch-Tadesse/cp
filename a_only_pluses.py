import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    a, b, c = map(int, input().split())

    ans = 0
    take = [0, 1, 2, 3, 4, 5]
    temp = []

    def back(i, temp):
        nonlocal ans
        if len(temp) == 3:
            if sum(temp) > 5:
                return
            coll = (a + temp[0]) * (b + temp[1]) * (c + temp[2])
            ans = max(ans, coll)
            return

        if i > 5:
            return

        for val in range(6):
            temp.append(val)
            back(i + 1, temp)
            temp.pop()

    back(0, temp)
    print(ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
