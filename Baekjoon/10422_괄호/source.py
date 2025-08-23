MOD = 1000000007

T = int(input())
numbers = [int(input()) for _ in range(T)]

max_num = max(numbers) // 2
dp = [0] * (max_num + 1)

dp[0] = 1
for i in range(1, max_num + 1):
    for j in range(i):
        dp[i] = (dp[i] + dp[j] * dp[i-1-j]) % MOD 

for num in numbers:
    print(0 if num % 2 else dp[num // 2])