N = int(input())
stairs = []

for _ in range(N):
    stairs.append(int(input()))

dp = [0] * N
dp[0] = stairs[0]
if N == 1:
    print(stairs[0])
else:
    dp[1] = stairs[0] + stairs[1]
    if N > 2:
        dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    print(dp[-1])