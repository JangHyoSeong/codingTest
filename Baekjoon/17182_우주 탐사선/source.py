N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(now, visited):
    if visited == (1 << N) - 1:
        return 0

    if dp[now][visited] != -1:
        return dp[now][visited]

    min_time = float('inf')
    for next in range(N):
        if not visited & (1 << next):
            time = graph[now][next] + dfs(next, visited | (1 << next))
            min_time = min(min_time, time)

    dp[now][visited] = min_time
    return min_time

print(dfs(K, 1 << K))
