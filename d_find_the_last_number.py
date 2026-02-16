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
    cand = list(range(1, n + 1))
    _max = (n + 1).bit_length()
    counter = [0] * _max
    for c in cand:
        for i in range(_max):
            counter[i] += c & (1 << i) != 0
    req = [i for i in range(1, n)]
    i = 0
    while len(cand) > 1:
        new_cand = []
        new_req = []
        new = 0
        ask = 1 << i
        has = set()
        for c in req:
            print(f"? {c} {ask}", flush=True)
            res = int(input())
            if res == 1:
                has.add(c)
            new += res
        if counter[i] == new:
            for c in req:
                if c not in has:
                    new_req.append(c)
            for c in cand:
                if c & ask == 0:
                    new_cand.append(c)
        else:
            new_req = list(has)
            for c in cand:
                if c & ask != 0:
                    new_cand.append(c)
        cand = new_cand
        req = new_req

    print(f"! {cand[0]}", flush=True)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
