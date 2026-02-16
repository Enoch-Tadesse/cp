import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , h = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    big = nums[0]
    small = nums[1]
    total = big + small
    time =  math.ceil(h / total)
    ans = time * total
    if time * 2 & 1:
        print(time * 2)
    else:
        if ans - small >= h:
            print(time * 2-1)
        else:
            print(time * 2)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
