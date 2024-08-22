str1 = list(input())
str2 = list(input())
N, M = len(str1), len(str2)
max_len = 0

dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if str1[i] == str2[j]:
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            max_len = max(dp[i][j], max_len)

print(max_len)
