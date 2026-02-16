import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , q = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    pre = [0] * (n + 2)
    for _ in range(q):
        a , b = list(map(int, input().split()))
        pre[a] += 1
        pre[b + 1] -= 1
    freq = [0] * n
    cur = 0
    for i in range(1, n + 1):
        cur += pre[i]
        freq[i - 1] = cur
    freq.sort(reverse=True)
    nums.sort(reverse=True)
    counter = 0
    for i in range(n):
        counter += freq[i] * nums[i]
    print(counter)



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
