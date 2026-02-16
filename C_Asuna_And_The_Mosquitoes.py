import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
import heapq
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    odds, evens = [], []
    for num in nums:
        if num & 1:
            odds.append(-1 * num)
        else:
            evens.append(-1 * num)
    heapq.heapify(odds)
    heapq.heapify(evens)
    curr = -1 * heapq.heappop(odds)
    while True:
        if curr & 1:
            if len(evens) == 0:
                break
            else:
                curr += 1
                temp = heapq.heappop(evens) + 1
                if temp != 0:
                    heapq.heappush(odds, temp)
        else:
            if len(odds) == 0:
                break
            else:
                curr += 1
                temp = heapq.heappop(odds) + 1
                if temp != 0:
                    heapq.heappush(evens, temp)
    if curr & 1 == 0:
        while len(odds) > 0:
            curr += -1 * heapq.heappop(odds)
    else:
        while len(evens) > 0:
            curr += -1 * heapq.heappop(evens)
    print(curr)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
