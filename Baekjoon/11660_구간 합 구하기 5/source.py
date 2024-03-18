N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
positions = [list(map(int, input().split())) for _ in range(M)]

prefix_sum = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = table[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

for i in range(M):
    y1, x1, y2, x2 = positions[i]
    result = prefix_sum[y2][x2] - prefix_sum[y2][x1-1] - prefix_sum[y1-1][x2] + prefix_sum[y1-1][x1-1]
    print(result)