def solution(info, n, m):
    INF = int(1e9)
    N = len(info)
    
    dp = [[INF] * m for _ in range(N+1)]
    dp[0][0] = 0
    
    for i in range(N):
        cost_a, cost_b = info[i]
        
        for b in range(m):
            if dp[i][b] == INF:
                continue
        
            if dp[i][b] + cost_a < n:
                dp[i+1][b] = min(dp[i+1][b], dp[i][b] + cost_a)
            
            if b + cost_b < m:
                dp[i+1][b + cost_b] = min(dp[i+1][b + cost_b], dp[i][b])
    result = min(dp[N])
    
    return result if result != INF else -1