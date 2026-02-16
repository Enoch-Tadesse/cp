import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    counts = [[], [], [], []]
    for i ,num in enumerate(nums):
        counts[num].append(i)
    cnt = min(len(counts[1]), len(counts[2]), len(counts[3]))
    print(cnt)
    for i in range(cnt):
        ans = []
        for idx in [1, 2, 3]:
            ans.append(counts[idx].pop() + 1)
        print(*ans)



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
