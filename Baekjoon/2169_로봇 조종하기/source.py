import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = table[0][0]

for j in range(1, M):
    dp[0][j] = dp[0][j-1] + table[0][j]

for i in range(1, N):
    left_to_right = [0] * M
    left_to_right[0] = dp[i-1][0] + table[i][0]

    for j in range(1, M):
        left_to_right[j] = max(left_to_right[j-1], dp[i-1][j]) + table[i][j]

    right_to_left = [0] * M
    right_to_left[M-1] = dp[i-1][M-1] + table[i][M-1]

    for j in range(M-2, -1, -1):
        right_to_left[j] = max(right_to_left[j+1], dp[i-1][j]) + table[i][j]
    
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])
    
print(dp[N-1][M-1])