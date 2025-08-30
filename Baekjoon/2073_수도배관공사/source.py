import sys

D, P = map(int, sys.stdin.readline().rstrip().split())
pipes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(P)]

dp = [-1] * (D + 1)
dp[0] = int(2e23)

for L, C in pipes:
    for s in range(D - L, -1, -1):
        if dp[s] == -1:
            continue
            
        new_cap = dp[s] if dp[s] < C else C
        if new_cap > dp[s+L]:
            dp[s+L] = new_cap

print(dp[D])