import sys
# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    g = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    deg = [len(g[i]) for i in range(n)]
    heap = []
    
    for i in range(n):
        if deg[i] == 1:
            heappush(heap, i)
    
    moves = 0
    
    while heap:
        ltr = []
        
        while heap and len(ltr) < k:
            leaf = heappop(heap)
            if deg[leaf] != 1:
                continue  
            ltr.append(leaf)
        
        if len(ltr) < k:
            break  
        
        moves += 1
        
        for leaf in ltr:
            deg[leaf] -= 1  
            for v in g[leaf]:
                if deg[v] > 0:
                    deg[v] -= 1  
                    if deg[v] == 1:
                        heappush(heap, v)  
    
    print(moves)
    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
