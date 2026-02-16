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
    if n <= 1:
        print(sum(nums))
        return
    alice1, bob1, alice2, bob2 = [], [], [], []
    og = 0
    for i, num in enumerate(nums):
        if (i + 1) & 1:
            og += num
            alice1.append(2 * num + (i + 1))
            alice2.append(2 * num - (i + 1))
        else:
            og -= num
            bob1.append(2 * num + (i + 1))
            bob2.append(2 * num - (i + 1))
    alice1.sort()
    alice2.sort()
    bob1.sort()
    bob2.sort()
    cand1 = og + bob1[-1] - alice1[0]
    cand2 = og + bob2[-1] - alice2[0]
    cand3 = og + ( n - 2 if n % 2 == 0 else n - 3)
    cand4 = og + (n - 1 if n & 1 else n - 2)
    print(max(og, cand1, cand2, cand3, cand4))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
