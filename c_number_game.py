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


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve():
    n = int(input())
    # whoever is on power of two losses
    game = ["Ashishgup", "FastestFinger"]
    if n == 1:
        print(game[1])
    elif n == 2:
        print(game[0])
    elif n == 3:
        print(game[0])
    else:
        if n & (n - 1) == 0:
            print(game[1])
        elif n % 2 == 0 and is_prime(n // 2):
            print(game[1])
        else:
            print(game[0])


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
