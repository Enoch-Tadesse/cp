import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    delta = [0] * (200000 + 2)
    n , m , q = list(map(int, input().split()))
    for _ in range(n):
        a, b = list(map(int, input().split()))
        delta[a] += 1
        delta[b + 1] -= 1
    pre = [0]
    for i in range(1, len(delta)):
        delta[i] += delta[i - 1]
        pre.append(pre[-1] + (delta[i] >= m))
        
    for _ in range(q):
        a , b = list(map(int, input().split()))
        print(pre[b] - pre[a - 1])


    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
