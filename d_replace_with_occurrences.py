import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math
from random import *

# input = input
input = sys.stdin.readline

big = randint(1000, 10 ** 9)

def rabbit(nums):
    seen = dict()
    for num in nums:
        if num == 1:
            continue
        if num ^ big in seen:
            seen[num ^ big] -= 1
            if seen[num ^ big] == 0:
                del seen[num ^ big]
        else:
            seen[num ^ big] = num - 1
    return sum(seen.values()) == 0


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    idx = defaultdict(list)
    ans = [0] * n
    label = 1
    for i , num in enumerate(nums):
        idx[num ^ big].append(i)
    for key , freq in idx.items():
        if key ^ big > len(freq) or len(freq) % (key ^ big) != 0:
            print("-1")
            return
        for j in range(1, len(freq) + 1):
            ans[freq[j - 1]] = label
            if j % (key ^ big) == 0:
                label += 1
    print(*ans)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
