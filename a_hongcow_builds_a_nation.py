import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def par(parent, num):
    if parent[num] != num:
        parent[num] = par(parent, parent[num])
    return parent[num]

def comb(num):
    return int(num * (num - 1) / 2)


def solve():
    n , m , k = list(map(int, input().split()))
    govs = list(map(int, input().split()))
    root = list(range(n+1))

    for _ in range(m):
        a , b = list(map(int, input().split()))
        roota = par(root, a)
        rootb = par(root, b)
        root[roota] = rootb
    size = [0] * (n + 1)
    for i in range(1, n + 1):
        r = par(root, i)
        size[r] += 1

    total = 0
    non = n
    largest = 0

    seen = set()
    for g in govs:
        r = par(root, g)
        if r in seen:
            continue
        seen.add(r)

        temp = size[r]
        total += comb(temp)
        non -= temp 
        largest = max(largest, temp)

    total -= comb(largest)
    total += comb(largest + non)

    print(total - m)
        


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
