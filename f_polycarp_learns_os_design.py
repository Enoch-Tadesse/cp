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
    words = []
    for _ in range(n):
        words.append(input().strip())
    q = int(input())
    for _ in range(q):
        query = input().strip()
        count = 0
        output = "-"
        for w in words:
            if query in w:
                count += 1
                output = w
        print(count, output)




def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
