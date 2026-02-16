import sys
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def solve():
    n, t = map(int, input().split())
    s = list(input().strip())

    for _ in range(t):
        i = 0
        while i < n - 1:
            if s[i] == 'B' and s[i + 1] == 'G':
                s[i], s[i + 1] = s[i + 1], s[i]
                i += 2  
            else:
                i += 1

    print(''.join(s))




def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
