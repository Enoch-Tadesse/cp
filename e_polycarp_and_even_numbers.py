import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    num = input().strip()
    if int(num[-1]) % 2 == 0:
        print(0)
        return
    if int(num[0]) % 2 == 0:
        # reverse the whole string
        print(1)
        return
    for n in num:
        if int(n) % 2 == 0:
            print(2)
            return
    print(-1)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
