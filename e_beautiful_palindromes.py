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

    counts = [0] * (n + 1)
    for num in nums:
        counts[num] += 1
    cand = []
    for i in range(1, n + 1):
        if counts[i] == 0:
            cand.append(i)
            break
    if not cand:
        for i in range(0, k):
            print(nums[i % n], end=" ")
        print()
    else:
        for i in range(1,n + 1):
            if i != cand[0] and i != nums[-1]:
                cand.append(i)
                break
        cand.append(nums[-1])
        for i in range(0 ,k):
            print(cand[i % 3], end=" ")
        print()



    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
