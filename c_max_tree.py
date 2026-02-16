import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    adj = defaultdict(lambda: [[], 0])  # how many owns me, who comes after me
    for _ in range(n - 1):
        a, b, x, y = list(map(int, input().split()))
        if x > y:
            adj[a][0].append(b)
            adj[b][1] += 1
        else:
            adj[b][0].append(a)
            adj[a][1] += 1
    q = deque([i for i in range(1, n + 1) if adj[i][1] == 0])
    ans = [0] * n
    val = n
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            ans[curr - 1] = val
            val -= 1
            for child in adj[curr][0]:
                adj[child][1] -= 1
                if adj[child][1] == 0:
                    q.append(child)
    print(*ans)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
