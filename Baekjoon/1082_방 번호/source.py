N = int(input())
price = list(map(int, input().split()))
money = int(input())

dp = [-10000] * (money+1)

for i in range(N-1, -1, -1):
    x = price[i]

    for j in range(x, money+1):
        dp[j] = max(dp[j], i, dp[j-x]*10+i)

print(dp[money])