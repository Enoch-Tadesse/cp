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
    nums = list(int(x) for x in input().strip())
    target = list(int(x) for x in input().strip())
    

    ones = target.count(1)
    zeros = n - ones

    state = 0
    for r in range(n - 1, -1, -1):
        if nums[r] ^ state == target[r]:
            ones -= nums[r] ^ state
            zeros -= nums[r] ^ state ^ 1
            continue
        if ones == zeros:
            ones -= nums[r] ^ state
            zeros -= nums[r] ^ state ^ 1
            ones, zeros = zeros , ones
            state ^= 1
        else:
            print("NO")
            return
    print("YES")



    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
