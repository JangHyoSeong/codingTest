N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (H+1)
dp[0] = 1

for block in blocks:
    new_dp = dp[:]
    for b in block:
        for h in range(H, b-1, -1):
            new_dp[h] = (new_dp[h] + dp[h-b]) % 10007
    dp = new_dp

print(dp[H])