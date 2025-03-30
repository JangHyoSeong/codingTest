INF = int(21e8)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(now, visited):
    if visited == (1 << N) - 1:
        return graph[now][0] if graph[now][0] > 0 else INF
    
    if dp[now][visited] != -1:
        return dp[now][visited]
    
    dp[now][visited] = INF
    
    for next in range(N):
        if visited & (1 << next) or graph[now][next] == 0:
            continue

        cost = graph[now][next] + tsp(next, visited | (1 << next))
        dp[now][visited] = min(dp[now][visited], cost)

    return dp[now][visited]

print(tsp(0, 1))