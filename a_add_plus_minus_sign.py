import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(int(x) for x in input().strip())
    curr = nums[0]
    for i in range(1, n):
        x = nums[i]
        if curr > 0:
            print('-', end="")
            curr -= x
        else:
            print('+', end="")
            curr += x
    print()
        
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
