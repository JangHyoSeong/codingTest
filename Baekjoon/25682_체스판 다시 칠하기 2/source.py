N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]

start_white = [[0] * M for _ in range(N)]
start_black = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        expected_w = "W" if (i + j) % 2 == 0 else "B"
        expected_b = "B" if (i + j) % 2 == 0 else "W"

        if board[i][j] != expected_w:
            start_white[i][j] = 1
        if board[i][j] != expected_b:
            start_black[i][j] = 1

def prefix_sum(arr):
    psum = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            psum[i+1][j+1] = arr[i][j] + psum[i][j+1] + psum[i+1][j] - psum[i][j]
    
    return psum

psum_w = prefix_sum(start_white)
psum_b = prefix_sum(start_black)

def get_sum(psum, x1, y1, x2, y2):
    return psum[x2][y2] - psum[x1][y2] -psum[x2][y1] + psum[x1][y1]

min_result = int(21e8)
for i in range(N - K + 1):
    for j in range(M - K + 1):
        sum_w = get_sum(psum_w, i, j, i+K, j+K)
        sum_b = get_sum(psum_b, i, j, i+K, j+K)
        min_result = min(min_result, sum_w, sum_b)

print(min_result)