import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math
from collections import deque

# input = input
input = sys.stdin.readline


def solve():
    adj = defaultdict(lambda: [[], 0])
    n, k = list(map(int, input().split()))
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        adj[a][0].append(b)
        adj[b][0].append(a)
        adj[a][1] += 1
        adj[b][1] += 1
    temp = []
    for i in range(1, n + 1):
        if adj[i][1] <= 1:
            temp.append(i)
    q = deque(temp)

    removed = 0
    seen = set(temp)
    for _ in range(k):
        if not q:
            break
        removed += len(q)
        for _ in range(len(q)):
            curr = q.popleft()
            nei, _ = adj[curr]
            for ele in nei:
                adj[ele][1] -= 1
                if ele not in seen and 0 <= adj[ele][1] <= 1:
                    q.append(ele)
                    seen.add(ele)
    input().strip()
    print(n - removed)
    return


def main():
    t = int(input())
    input().strip()
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
