A = input()
B = input()

len_A = len(A)
len_B = len(B)

dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = len_A, len_B
answer = []

while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        answer.append(A[i-1])
        i -= 1
        j -= 1
    
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

answer.reverse()
print(''.join(answer))