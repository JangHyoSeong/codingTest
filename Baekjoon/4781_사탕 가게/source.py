while True:
    N, M = input().split()
    N = int(N)
    M = float(M)

    if N == 0 and M == 0.00:
        break

    M = int(M * 100 + 0.5)
    candies = []
    for _ in range(N):
        c, p = input().split()
        c = int(c)
        p = float(p)
        p = int(p * 100 + 0.5)
        candies.append((p, c))

    dp = [0] * (M + 1)

    for p, c in candies:
        for money in range(p, M + 1):
            dp[money] = max(dp[money], dp[money - p] + c)

    print(dp[M])