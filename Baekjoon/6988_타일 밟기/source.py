from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))

dp = defaultdict(dict)

max_sum = 0

for i in range(N):
    for j in range(i):
        d = arr[i] - arr[j]

        if j in dp[d]:
            new_sum = dp[d][j] + arr[i]
            new_len = 3
        else:
            new_sum = arr[j] + arr[i]
            new_len = 2

        if new_len >= 2:
            dp[d][i] = max(dp[d].get(i, 0), new_sum)

        if new_len >= 3:
            max_sum = max(max_sum, new_sum)

print(max_sum)