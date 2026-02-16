import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def bs(k):
    l , r = 1, k * 100000
    while l <= r:
        mid = (l + r) // 2
        if math.comb(mid, 3) >= k:
            r = mid - 1
        else:
            l = mid + 1
    return l

def solve():
    k = int(input())
    size = bs(k)
    ans = [['1'] * size for _ in range(size)]
    for i in range(size):
        ans[i][i] = '0'
    _max = math.comb(size, 3)
    if abs(_max - k) & 1:
        print(-1)
        return
    l , r = 0 , size - 1
    while _max - k > 0:
        if l == r:
            break
        _max -= 2
        ans[l][r] = '0'
        ans[r][l] = '0'
        l += 1
        r -= 1
    for a in ans:
        print("".join(a))
    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
