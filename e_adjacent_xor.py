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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a[-1] != b[-1]:
        print("NO")
        return
    for i in range(n - 2, -1, -1):
        if a[i] == b[i] or a[i] ^ a[i + 1] == b[i] or a[i] ^ b[i + 1] == b[i]:
            continue
        print("NO")
        return
    print("YES")




def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
