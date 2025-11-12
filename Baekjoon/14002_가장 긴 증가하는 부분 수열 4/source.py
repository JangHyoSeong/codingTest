N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N
prev = [-1] * N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

max_len = max(dp)
index = dp.index(max_len)

lis = []
while index != -1:
    lis.append(arr[index])
    index = prev[index]

lis.reverse()
print(max_len)
print(" ".join(map(str, lis)))