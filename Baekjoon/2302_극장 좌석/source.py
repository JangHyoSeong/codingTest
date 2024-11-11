N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]

sections = []
if M > 0:
    sections.append(vips[0] - 1)
    for i in range(1, M):
        sections.append(vips[i] - vips[i-1] - 1)
    sections.append(N - vips[-1])
else:
    sections.append(N)
max_length = max(sections)

dp = [1] * (max_length+1)
for i in range(2, max_length+1):
    dp[i] = dp[i-1] + dp[i-2]

result = 1
for section in sections:
    result *= dp[section]

print(result)