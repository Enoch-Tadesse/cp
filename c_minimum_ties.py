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
    games = (n ) * (n - 1) // 2
    if n & 1 == 0:
        print(*([0] * games))
        return
    ans = []
    cnt = [0] * (games + 1)
    total = (n - 1) // 2
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if cnt[i] < total:
                ans.append(1)
                cnt[i] += 1
            else:
                cnt[j] += 1

                ans.append(-1)
    print(*ans)




def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
