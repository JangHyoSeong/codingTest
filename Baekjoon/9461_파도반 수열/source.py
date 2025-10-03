T = int(input())
arr = [int(input()) for _ in range(T)]
max_n = max(arr)

dp = [1] * (max_n + 1)

for i in range(4, max_n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

for n in arr:
    print(dp[n])