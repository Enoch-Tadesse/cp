import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    mods = dict()
    for num in nums:
        r = num % k
        mods[r] = mods.get(r, 0) + 1
    if 0 in mods:
        print(0)
        return
    if k == 2:
        print(1)
    elif k == 3:
        if 2 in mods: print(1)
        else: print(2)
    elif k == 4:
        if 2 in mods and mods[2] >=2:
            print(0)
        elif 3 in mods:
            print(1)
        else:
            cand = mods.get(2, 0)
            if 1 in mods and mods[1] + cand >= 2:
                print(max(0, 2 - cand))
            else:
                print(3)
    elif k == 5:
        for i in range(4, -1, -1):
            if i in mods:
                print(5 - i)
                break

    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
