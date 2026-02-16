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
    a = list(x for x in input().strip())
    q = deque(a)
    m = int(input())
    b = list(x for x in input().strip())
    turn = list(x for x in input().strip())
    i = 0
    for t in turn:
        if t == "V":
            q.appendleft(b[i])
        else:
            q.append(b[i])
        i += 1
    print("".join(list(q)))
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
