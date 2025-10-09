import math

N, K = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

min_std = float('inf')

for length in range(K, N + 1):
    for start in range(0, N - length + 1):
        end = start + length
        now_sum = prefix_sum[end] - prefix_sum[start]
        now_avg = now_sum / length

        now_var_sum = 0
        for j in range(start, end):
            now_var_sum += (arr[j] - now_avg) ** 2
        now_var = now_var_sum / length
        now_std = math.sqrt(now_var)

        if now_std < min_std:
            min_std = now_std

print(min_std)