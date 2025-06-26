T, W = map(int, input().split())
arr = [int(input()) for _ in range(T)]

dp = [[0] * (T+1) for _ in range(W+1)]

for t in range(1, T+1):
    fruit = arr[t-1]

    for w in range(W+1):
        if w == 0:
            dp[w][t] = dp[w][t-1] + (1 if fruit == 1 else 0)
        
        else:
            current_tree = (w % 2) + 1
            dp[w][t] = max(dp[w][t-1], dp[w-1][t-1]) + (1 if fruit == current_tree else 0)

print(max(dp[w][t] for w in range(W+1)))