N, D = map(int, input().split())

shortcuts = {}
for _ in range(N):
    a, b, c = map(int, input().split())
    if shortcuts.get(a) is None:
        shortcuts[a] = [(b, c)]
    else:
        shortcuts[a].append((b, c))

dp = [i for i in range(D+1)]

for i in range(D+1):
    dp[i] = min(dp[i-1] + 1, dp[i])

    if shortcuts.get(i) is not None:
        for next, dist in shortcuts[i]:
            if next <= D:
                dp[next] = min(dp[next], dp[i] + dist)

print(dp[-1])