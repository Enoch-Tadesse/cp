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
    counter = [0] * (n + 1)

    for num in nums:
        counter[num] += 1
    pre = counter[:]
    for i in range(1, len(pre)):
        pre[i] += pre[i - 1]
    ans = 0
    for g in range(1, n+1):
        idx = min(n, 4 * g - 1)
        good = n - pre[idx]
        if g <= n:
            good += counter[g]
        if 2 * g <= n:
            good += counter[2 * g]
        if 3 * g <= n:
            good += counter[3 * g]
        if good >= n - k:
            ans = g
    print(ans)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
