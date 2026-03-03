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
    s = list(x for x in input().strip())
    t = list(x for x in input().strip())
    cnt_s = Counter(s)
    cnt_t = Counter(t)

    for k ,v in cnt_s.items():
        if k not in cnt_t:
            print("Impossible")
            return
        if v > cnt_t[k]:
            print("Impossible")
            return
        cnt_t[k] -= v

    t = []
    for k , v in cnt_t.items():
        t.extend([k] * cnt_t[k])

    t.sort()

    ans = []
    i , j = 0 , 0
    while i < len(s) and j < len(t):
        if s[i] <= t[j]:
            ans.append(s[i])
            i += 1
        else:
            ans.append(t[j])
            j += 1

    ans.extend(s[i:])
    ans.extend(t[j:])
    print("".join(ans))



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
