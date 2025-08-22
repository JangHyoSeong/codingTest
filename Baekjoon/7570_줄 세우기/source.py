import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * (N + 2)
max_length = 0

for num in arr:
    dp[num] = dp[num - 1] + 1
    if dp[num] > max_length:
        max_length = dp[num]

print(N - max_length)