import sys
sys.setrecursionlimit(int(1e9))

N = int(sys.stdin.readline().rstrip())
towns = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

dp = [[0, 0] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(u):
    visited[u] = True
    dp[u][0] = 0
    dp[u][1] = towns[u]

    for v in edges[u]:
        if not visited[v]:
            dfs(v)
            dp[u][0] += max(dp[v][0], dp[v][1])
            dp[u][1] += dp[v][0]

dfs(1)
print(max(dp[1][0], dp[1][1]))