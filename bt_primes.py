import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

_max = 10**6 + 1
prime = [True] * _max
prime[0] = prime[1] = False
for i in range(2, int(_max**0.5) + 1):
    if prime[i]:
        for j in range(i * i, _max, i):
            prime[j] = False


def perfect(x: int) -> int:
    root = int(x**0.5)
    return root * root == x, root


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        ok, root = perfect(num)
        if ok and prime[root]:
            print("YES")
        else:
            print("NO")


def main():
    t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
