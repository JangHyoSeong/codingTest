T = int(input())
numbers = [int(input()) for _ in range(T)]

max_num = max(numbers)
dp = [1] * (max_num + 1)

dp[1] = 1

if max_num > 1:
    dp[2] = 2
if max_num > 2:
    dp[3] = 4

for i in range(4, max_num+1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

for number in numbers:
    print(dp[number])