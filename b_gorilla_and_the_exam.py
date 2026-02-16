import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

from random import randint

# input = input
input = sys.stdin.readline

big = randint(1, 10 ** 8)

def solve():
    n , k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    if k == 0:
        print(len(set(nums)))
        return
    counts = {}
    for num in nums:
        counts[num ^ big] = counts.get(num ^ big, 0) + 1
    cnts = [f for k , f in counts.items()]
    cnts.sort()
    i = 0
    curr = 0
    while i < len(cnts):
        if curr + cnts[i] <= k:
            curr += cnts[i]
        else:
            break
        i += 1
    print(max(len(cnts) - i, 1))


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
