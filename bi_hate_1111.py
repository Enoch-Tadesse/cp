import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    nums = int(input())
    _max = 11 * 111 - 11 - 111 + 1
    if nums >= _max:
        print("YES")
        return
    limit = _max // 11 + 1
    for a in range(limit):
        for b in range(limit):
            cand = a * 11 + b * 111
            if cand > nums:
                break
            if cand == nums:
                print("YES")
                return
    print("NO")
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
