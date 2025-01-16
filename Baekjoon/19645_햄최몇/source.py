N = int(input())
burgers = list(map(int, input().split()))

sum_burgers = sum(burgers)
dp = [[False] * (sum_burgers + 1) for _ in range(sum_burgers + 1)]
dp[0][0] = True

current_sum = 0
max_util = 0

for burger in burgers:
    current_sum += burger
    for i in range(current_sum, -1, -1):
        for j in range(current_sum, -1, -1):
            if dp[i][j]:
                dp[i+burger][j] = True
                dp[i][j+burger] = 1

for i in range(sum_burgers + 1):
    for j in range(sum_burgers + 1):
        if not dp[i][j]:
            continue

        k = sum_burgers - (i+j)
        min_util = min(k, i, j)
        max_util = max(max_util, min_util)

print(max_util)