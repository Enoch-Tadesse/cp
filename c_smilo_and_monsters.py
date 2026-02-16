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
    nums = list(map(int, input().split()))
    nums.sort()
    l = 0
    r = n - 1
    cnt = 0

    # maintain two heaps
    # biggest and smallest
    # keep an array of dead hordes
    deads = [False] * n
    _min = []
    _max = []
    dcnt = 0
    total = sum(nums)

    curr = 0
    while dcnt != total:

        while _max and deads[_max[0][0]]:
            heappop(_max)
        _max_i, _max_ele = _max[0]

        while True and _max and _min:
            while deads[_min[0][0]]:
                heappop(_min)

            _min_i, _min_ele = _min[0]
            if _min_ele + curr <= _max_ele:
                dcnt -= _min_ele
                curr += _min_ele
                cnt += _min_ele
                deads[_min_i] = True
                heappop(_min)
            else:
                need = _max_ele - curr
                _new_min = _min_ele - need
                cnt += need + 1
                heappop(_min)
                heappush(_min, (_new_min, _min_i))
                heappop(_max)
                break
        print(cnt)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
