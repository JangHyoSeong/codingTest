N, M, K = map(int, input().split())

def count_paths(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                continue

            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n][m]

if K == 0:
    print(count_paths(N, M))

else:
    kr = (K-1) // M + 1
    kc = (K-1) % M + 1

    paths1 = count_paths(kr, kc)
    paths2 = count_paths(N-kr+1, M-kc+1)

    print(paths1 * paths2)