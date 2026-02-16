import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def get_twos(num):
    counter = 0
    while num & 1 == 0:
        counter += 1
        num >>= 1
    return counter

def solve():
    n = int(input())
    k = 1 << n
    nums = list(map(int, input().split()))
    evens = sum(get_twos(num) for num in nums if num & 1 == 0)
    if evens >= n:
        print(0)
        return
    need = n - evens
    avail = list(range(1, n + 1))
    twos = [get_twos(num) for num in avail]
    pair = list(zip(twos, avail))
    pair.sort(reverse=True)
    pre = 0
    for i in range(len(pair)):
        pre += pair[i][0]
        if pre >= need:
            print(i + 1)
            return
    print(-1)



def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
