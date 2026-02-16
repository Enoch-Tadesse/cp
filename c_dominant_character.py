import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    chars = input().strip()
    ans = float("inf")
    for i in range(n):
        cnt = [0] * 3
        c = chars[i]
        cnt[ord(c) - ord('a')] += 1
        for j in range(i + 1, min(n, i + 7)):
            cnt[ord(chars[j]) - ord('a')] += 1
            if cnt[0] > cnt[1] and cnt[0] > cnt[2]:
                ans = min(ans, j - i + 1)
    print(ans if ans != float("inf") else -1)




def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
