N = int(input())
open1, open2 = map(int, input().split())

M = int(input())
arr = [int(input()) for _ in range(M)]

dp = [[[float('inf')] * (N + 1) for _ in range(N + 1)] for _ in range(M + 1)]
dp[0][open1][open2] = 0

for i in range(M):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if dp[i][j][k] != float('inf'):
                current_use = arr[i]

                # 문 j를 current_use로 이동
                dp[i + 1][current_use][k] = min(dp[i + 1][current_use][k], dp[i][j][k] + abs(j - current_use))
                
                # 문 k를 current_use로 이동
                dp[i + 1][j][current_use] = min(dp[i + 1][j][current_use], dp[i][j][k] + abs(k - current_use))

result = float('inf')
for j in range(1, N+1):
    for k in range(1, N+1):
        result = min(result, dp[M][j][k])

print(result)