import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


# if there is a concrete value, get it and check if possible or not, result is binary
# 
def solve():
    n , k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    found = False
    due = 0
    for i in range(n):
        if b[i] != -1:
            if found:
                if due != a[i] + b[i]:
                    print(0)
                    return
            else:
                found = True
                due = a[i] + b[i]
        else:
            if found:
                if due - a[i] > k or due-a[i] < 0:
                    print(0)
                    return
    if found:
        print(1)
        return
    cap = max(a)
    if k == cap:
        print(1)
        return
    low = min(a)
    print(k - low - cap + 3)
        
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
