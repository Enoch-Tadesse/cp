import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    q = int(input())
    
    a1, a2 = 1, 1
    fore = False
    found = False
    for _ in range(q):
        d, k , word = list(map(str, input().split()))
        if found:
            print("YES")
            continue
        ass = word.count("a")
        if d == "1":
            a1 += ass * int(k)
            if ass != len(word):
                fore = True
        if d == "2":
            if ass != len(word):
                print("YES")
                found = True
                continue
            a2 += word.count("a") * int(k)
        if fore or a1 >= a2:
            print("NO")
        else:
            print("YES")
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
