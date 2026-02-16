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
    nums = list(map(int, input().split()))
    evens = [num for num in nums if num % 2 == 0]
    if len(evens) >= 2:
        print(*evens[:2])
        return
    elif len(evens) == 1:
        key = evens[0]
        for num in nums:
            if num != key and key > num and (key % num) % 2 == 0:
                print(min(num, key), max(num, key))
                return
    odds = [num for num in nums if num % 2 == 1]
    for i in range(1, len(odds)):
        if odds[i] % odds[i - 1] % 2 == 0:
            print(odds[i - 1], odds[i])
            return
    _max = min(len(odds), 35)

    for i in range(_max):
        for j in range(i + 1, _max):
            x, y = odds[i], odds[j]
            if y % x % 2 == 0:
                print(x, y)
                return

    print(-1)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
