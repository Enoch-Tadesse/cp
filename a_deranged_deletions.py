import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    if nums == list(sorted(nums)):
        print("NO")
        return
    second = list(sorted(nums))
    coll = []
    for i in range(n):
        if nums[i] == second[i]:
            continue
        coll.append(nums[i])
    print("YES")
    print(len(coll))
    print(*coll)

def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
