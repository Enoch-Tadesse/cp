import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def isPrime(number):
    if number == 1:
        return True
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def solve():
    n = int(input())
    for i in range(1, n // 2 + 1):
        if not isPrime(i) and not isPrime(n - i):
            print(i, n - i)
            return
    print(0, 0)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
