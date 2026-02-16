import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right, insort
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    news = []
    ans = []
    for i , num in enumerate(nums):
        idx = bisect_right(news, num)
        if idx != 0:
            ans.append(i + 1)
        else:
            insort(news, num)
    print(len(ans))
    print(*ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
