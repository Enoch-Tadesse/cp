import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def can_sort(n, a, b_val):
    if n == 1:
        return True

    prev0_possible = True
    prev0_val = a[0]
    prev1_possible = True
    prev1_val = b_val - a[0]

    for i in range(1, n):
        cx0 = a[i]
        cx1 = b_val - a[i]
        new_prev0 = False
        new_prev1 = False

        if prev0_possible and cx0 >= prev0_val:
            new_prev0 = True
        if prev1_possible and cx0 >= prev1_val:
            new_prev0 = True

        if prev0_possible and cx1 >= prev0_val:
            new_prev1 = True
        if prev1_possible and cx1 >= prev1_val:
            new_prev1 = True

        prev0_possible, prev1_possible = new_prev0, new_prev1
        prev0_val = cx0
        prev1_val = cx1

        if not (prev0_possible or prev1_possible):
            return False

    return prev0_possible or prev1_possible


def solve():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    l, r = 0, len(b) - 1
    while l <= r:
        mid = (r + l) // 2
        if can_sort(n, a, b[mid]):
            print("")
            return
        else:
            r = mid - 1
    print("NO")
    return


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
