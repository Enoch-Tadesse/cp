
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, adj):
    n = len(adj)
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])
    farthest_node = start

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > dist[farthest_node]:
                    farthest_node = v
    return farthest_node, dist[farthest_node]

def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    u, _ = bfs(1, adj)
    _, diameter = bfs(u, adj)
    print(diameter)

if __name__ == "__main__":
    solve()
