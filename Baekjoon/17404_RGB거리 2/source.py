import sys

N = int(sys.stdin.readline().rstrip())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

INF = float('inf')
result = INF

for first_color in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    
    dp[0][first_color] = costs[0][first_color]
    
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    for last_color in range(3):
        if first_color != last_color:
            result = min(result, dp[N-1][last_color])

print(result)