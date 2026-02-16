import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , i = list(map(int, input().split()))
    cons = list(x for x in input().strip())
    counts = Counter(['A', "B", "C", "D", "E", "F","G"])
    for c in cons:
        counts[c] += 1
    ans = 0
    for key, val in counts.items():
        if val <= i:
            ans += i - val + 1
    print(ans)


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
