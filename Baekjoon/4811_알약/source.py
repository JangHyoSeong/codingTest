arr = []
while True:
    n = int(input())
    if n:
        arr.append(n)
    else:
        break

max_num = max(arr)

dp = [0] * (max_num + 1)
dp[0] = 1
for i in range(1, max_num+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-1-j]

for num in arr:
    print(dp[num])