import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , s = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    total = sum(nums)
    if s < total:
        print(*nums)
        return
    if s == total:
        print(-1)
        return
    last = [1, 2, 3]
    found = False
    if (s - total) % last[0] != 0:
        nums.remove(0)
        nums.remove(1)
        nums.extend([0, 1])
        found = True
    elif (s - total) % last[1] != 0:
        nums.remove(2)
        nums.remove(0)
        nums.extend([2, 0])
        found = True
    elif (s - total) % last[2] != 0:
        nums.remove(2)
        nums.remove(1)
        nums.extend([2, 1])
        found = True
    if found:
        print(*nums)
    else:
        print(-1)





def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
