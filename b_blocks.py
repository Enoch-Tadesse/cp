import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def can(chars):
    ans = [-1, []]
    for i in range(len(chars) - 1):
        if chars[i] == 1:
            continue
        chars[i] = 1
        chars[i + 1] ^= 1
        ans[1].append(i + 1)
    if (int(chars[-1]) == 0):
        return ans
    ans[0] = len(ans[1])
    return ans

def solve():
    n = int(input())
    chars = list(x for x in input().strip())
    first = [c == "B" for c in chars]
    a , b = can(first[:])
    if a != -1:
        print(a)
        print(*b)
        return
    second = [i ^ 1 for i in first]
    a , b = can(second[:])
    if a != -1:
        print(a)
        print(*b)
        return
    print(-1)


    

    


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
