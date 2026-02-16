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
    nums = list(map(int, input().split()))
    evens = []
    odds = []
    for num in nums:
        if num & 1:
            odds.append(num)
        else:
            evens.append(num)
    evens.sort()
    odds.sort()
    i = j = 0
    ans = []
    for num in nums:
        if num & 1:
            ans.append(odds[i])
            i += 1
        else:
            ans.append(evens[j])
            j += 1
    print("YES" if ans == sorted(ans) else "NO")


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
