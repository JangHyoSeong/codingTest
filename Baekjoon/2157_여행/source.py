import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a < b:
        edges[a].append((b, c))

dp = [[-1] * (M+1) for _ in range(N+1)]
dp[1][1] = 0

for cnt in range(1, M):
    for curr in range(1, N+1):
        if dp[curr][cnt] == -1:
            continue

        for next_city, score in edges[curr]:
            dp[next_city][cnt + 1] = max(dp[next_city][cnt + 1], dp[curr][cnt] + score)
    
print(max(dp[N]))