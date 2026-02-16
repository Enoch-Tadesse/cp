import sys
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n , e = list(map(int, input().split()))
    colors = list(x for x in input().strip())
    adj = defaultdict(lambda : [[], 0])
    freq = [[0] * 26 for _ in range(n + 1)]
    offset = ord('a')
    for _ in range(e):
        a , b = list(map(int, input().split()))
        adj[a][0].append(b)
        adj[b][1] += 1
    q = deque()
    for i in range(1, n+1):
        if adj[i][1] == 0:
            q.append(i)
    if len(q) == 0:
        print(-1)
        return
    ans = 0
    seen = set()
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            seen.add(curr)
            freq[curr][ord(colors[curr-1]) - offset] += 1 
            for child in adj[curr][0]:
                adj[child][1] -= 1 
                if adj[child][1] == 0:
                    q.append(child)
                for i in range(26):
                    freq[child][i] = max(freq[child][i], freq[curr][i])
            ans = max(ans, max(freq[curr]))
    print(ans if len(seen) == n else -1) 


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
