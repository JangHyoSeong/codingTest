N = int(input())
left_cards = list(map(int, input().split()))
right_cards = list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
        if left_cards[i] > right_cards[j]:
            dp[i][j] = max(dp[i][j], dp[i][j+1] + right_cards[j])

print(dp[0][0])