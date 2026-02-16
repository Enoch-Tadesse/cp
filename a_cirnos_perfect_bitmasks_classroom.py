import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    x = int(input())
    if x & 1:
        if (x >> 1) != 0:
            print(1)
            return
        else:
            print(3)
            return
    cnt = 0
    while x & 1 == 0:
        cnt += 1
        x = x >> 1
    if x != 1:
        print(1 << cnt)
        return
    ans = 1
    ans |= 1 << cnt
    print(ans)




def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
