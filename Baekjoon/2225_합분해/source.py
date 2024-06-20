N, K = map(int, input().split())

# DP 테이블 초기화
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

# DP 테이블 채우기
for j in range(1, K + 1):
    for i in range(N + 1):
        for x in range(N + 1):
            if i >= x:
                dp[i][j] = (dp[i][j] + dp[i - x][j - 1]) % 1000000000

# 결과 출력
print(dp[N][K])