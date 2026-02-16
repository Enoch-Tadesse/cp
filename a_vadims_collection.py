import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    nums = list(int(x) for x in input().strip())
    ans = []
    for i in range(9 , -1, -1):
        if i in nums:
            ans.append(nums.pop(nums.index(i)))
        else:
            nums.sort()
            idx = bisect_right(nums, i)
            ans.append(nums.pop(idx))
    for i in range(len(ans)):
        ans[i] = str(ans[i])
    print("".join(ans))
        

    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
