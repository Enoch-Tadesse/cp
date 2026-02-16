import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def valid(guess, m, coll):
    counter = 0
    for t, z, y in coll:
        full = t * z + y
        counter += (guess // full) * z
        counter += min((guess % full) // t, z)
    return counter >= m


def contri(guess, coll, needed):
    made = 0
    for t, z, y in coll:
        if made >= needed:
            print(0, end=" ")
            continue
        total = 0
        full = t * z + y
        total += (guess // full) * z
        total += min((guess % full) // t, z)
        total = min(total, needed - made)
        made += total
        print(total, end=" ")
    print()


def solve():
    m, n = list(map(int, input().split()))
    coll = []
    for _ in range(n):
        coll.append(list(map(int, input().split())))
    l, r = 0, 10**18 + 1
    while l <= r:
        mid = l + (r - l) // 2
        if valid(mid, m, coll):
            r = mid - 1
        else:
            l = mid + 1
    print(l)
    contri(l, coll, m)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
