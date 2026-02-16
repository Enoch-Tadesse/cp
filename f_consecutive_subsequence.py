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

    last = dict()
    size = dict()
    par = dict()

    for i, num in enumerate(nums):
        par[i] = i
        size[i] = 1

    for i, num in enumerate(nums):
        if num - 1 in last:
            if size[last[num - 1]] + 1 > size[i]:
                par[i] = last[num - 1]
                size[i] = size[last[num - 1]] + 1
            # size[num] = max(size.get(num, 0), size[num - 1]) + 1
        last[num] = i
    x = max(size.values())
    y = 0
    for k , v in size.items():
        if v == x:
            y  = k
            break
    print(x)
    init = y
    ans = [init]
    while par[init] != init:
        ans.append(par[init])
        init = par[init]
    ans = ans[::-1]
    print(*[a + 1 for a in ans])




def main():
    t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
