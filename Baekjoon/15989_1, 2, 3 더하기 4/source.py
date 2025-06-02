import sys

T = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

dp_len = max(arr)
dp = [0] * (dp_len + 1)

dp[0] = 1

for num in [1, 2, 3]:
    for i in range(num, dp_len + 1):
        dp[i] += dp[i - num]

for n in arr:
    print(dp[n])