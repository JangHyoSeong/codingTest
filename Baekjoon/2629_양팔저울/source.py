N = int(input())
weights = list(map(int, input().split()))

sum_weights = sum(weights)

dp = [[False] * (sum_weights + 1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    weight = weights[i]
    for w in range(sum_weights, -1, -1):
        if dp[i][w]:
            dp[i+1][w] = True
            if w + weight <= sum_weights:
                dp[i+1][w+weight] = True
            dp[i+1][abs(w-weight)] = True

result = []
M = int(input())
arr = list(map(int, input().split()))

for number in arr:
    if number <= sum_weights and dp[N][number]:
        result.append("Y")
    else:
        result.append("N")

print(" ".join(map(str, result)))