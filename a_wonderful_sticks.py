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
    orders = list(x for x in input().strip())
    ans = [0] * n
    curr = n
    for i in range(n - 2, -1, -1):
        if orders[i] == ">":
            ans[i + 1] = curr
            curr -= 1
    curr = 1
    for i in range(n - 1, -1, -1):
        if ans[i] == 0:
            ans[i] = curr
            curr += 1
    print(*ans)
    





def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
