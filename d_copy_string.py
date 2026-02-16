import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n, k = list(map(int, input().split()))
    init = list(x for x in input().strip())
    target = list(x for x in input().strip())
    if init[0] != target[0]:
        print(-1)
        return
    if init == target:
        print(0)
        return
    moves = 0
    ans = []
    checker = "".join(target)
    while moves < k:
        idx_move = set()
        for i in range(1, n):
            if init[i] != target[i]:
                idx_move.add(i)
        if not idx_move:
            break
        new_init = init[:]
        for i in sorted(idx_move):
            if i > 0:
                new_init[i] = init[i - 1]
        moves += 1
        init = new_init
        ans.append("".join(init))
        if ans[-1] == checker:
            break
    if ans[-1] != checker:
        print(-1)
        return
    print(len(ans))
    for a in ans:
        print(a)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
