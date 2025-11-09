MOD = 1234567

T = int(input())
cases = [int(input()) for _ in range(T)]

adj = {
    0: [7],
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8, 0],
    8: [5, 7, 9],
    9: [6, 8],
}

max_N = max(cases)
dp = [[0] * 10 for _ in range(max_N + 1)]

for num in range(10):
    dp[1][num] = 1

for i in range(2, max_N + 1):
    for num in range(10):
        dp[i][num] = sum(dp[i-1][j] for j in adj[num]) % MOD

for n in cases:
    print(sum(dp[n]) % MOD)