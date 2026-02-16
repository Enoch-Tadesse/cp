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
    nums = list(map(int, input().split()))
    stack = [nums[0]]
    ans = []

    for i in range(1, n):
        last = stack[-1]
        if stack[-1] > nums[i]:
            stack.append(nums[i])
            continue
        while stack and stack[-1] < nums[i]:
            ans.append((stack[-1], nums[i]))
            stack.pop()
        stack.append(last)
    if len(stack) != 1:
        print("NO")
    else:
        print("YES")
        for a in ans:
            print(*a)
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
