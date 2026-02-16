# ---------- Tarjan's Algorithm for Bridges ----------
tin = {}
low = {}
timer = [0]
visited = set()

critical = []
def dfs(curr, prev):
    tin[curr] = low[curr] = timer[0]
    timer[0] += 1
    visited.add(curr)

    for nei in adj[curr]:
        if nei == prev:
            continue
        if nei in visited:
            low[curr] = min(low[nei], low[curr])
        else:
            dfs(nei, curr)
            low[curr] = min(low[nei], low[curr])
            if low[nei] > tin[curr]:
                critical.append([nei, curr])

for i in range(n):
    if i not in visited:
        dfs(i, -1)

return critical
