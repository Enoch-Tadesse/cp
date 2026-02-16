import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def root(parent, x):
    if parent[x] == x:
        return x
    parent[x] = root(parent, parent[x])
    return parent[x]

def inc(parent, score, b , key):
    for k , p in parent.items():
        if p == key:
            score[k] += b
    return
def solve():
    n , k = list(map(int, input().split()))
    score = defaultdict(int)
    parent = defaultdict(int)
    for _ in range(k):
        arr = input().split() 
        if len(arr) > 2:
            ins , a , b = arr
            a = int(a)
            b = int(b)
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            if ins == "join":
                roota = root(parent, a)
                rootb = root(parent, b)
                parent[roota] = rootb
            else:
                inc(parent, score, b, root(parent, a))
        else:
            print(score[int(arr[1])])


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
