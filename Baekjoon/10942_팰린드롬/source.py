N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())
questions = [list(map(int, input().split())) for _ in range(M)]

dp = [[False] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][i] = True

for i in range(1, N):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = True

for length in range(3, N+1):
    for i in range(1, N-length+2):
        j = i + length - 1
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = True

for question in questions:
    s, e = question
    if dp[s][e]:
        print(1)
    else:
        print(0)