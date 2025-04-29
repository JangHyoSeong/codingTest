import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    K = int(sys.stdin.readline().rstrip())
    files = list(map(int, sys.stdin.readline().rstrip().split()))

    prefix_sum = [0] * (K+1)
    for i in range(K):
        prefix_sum[i+1] = prefix_sum[i] + files[i]
    
    dp = [[0] * K for _ in range(K)]

    for length in range(2, K+1):
        for i in range(K - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + (prefix_sum[j+1] - prefix_sum[i])
                if cost < dp[i][j]:
                    dp[i][j] = cost
    print(dp[0][K-1])