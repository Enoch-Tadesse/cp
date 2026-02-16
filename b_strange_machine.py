import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, q = list(map(int, input().split()))
    seq = list(x for x in input().strip())
    query = list(map(int, input().split()))
    cho = seq.count("B")
    if cho == 0:
        for num in query:
            print(num)
    else:
        for num in query:
            i = 0
            counter = 0
            while num > 0:
                i = i % n
                if seq[i] == "A":
                    num -= 1
                else:
                    num //= 2
                counter += 1
                i += 1
            print(counter)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
