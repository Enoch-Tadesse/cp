import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , t, s = list(map(int, input().split()))
    teach = list(map(int, input().split()))
    studs = list(map(int, input().split()))
    teach.sort()
    for i , st in enumerate(studs):
        right = bisect_right(teach, st)
        if right == t:
            print(n - teach[right - 1] )
        elif right == 0:
            print(teach[0] - 1)
        else:
            print((teach[right] - teach[right - 1]) // 2)
        


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
