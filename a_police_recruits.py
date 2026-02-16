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
    counter = 0
    
    av = 0
    for num in nums:
        if num == -1:
            if av == 0:
                counter += 1
            else:
                av -= 1
            continue
        av += num
    print(counter)


def main():
    t = 1
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
