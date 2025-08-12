N = int(input())

papers = []
for _ in range(N):
    a, b = map(int, input().split())
    w, h = min(a, b), max(a, b)
    papers.append((w, h))

papers.sort(key=lambda x: (-x[0], -x[1]))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if papers[i][0] <= papers[j][0] and papers[i][1] <= papers[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))