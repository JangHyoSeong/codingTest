N = int(input())
arr = [list(map(int, input().split())) for _ in range(N*N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

table = [[0] * N for _ in range(N)]
likes = {}

for student, *prefer in arr:
    likes[student] = prefer
    candidate = []

    for x in range(N):
        for y in range(N):
        
            if table[x][y] != 0:
                continue

            like_count = 0
            empty_count = 0

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if table[nx][ny] in prefer:
                        like_count += 1
                    
                    if table[nx][ny] == 0:
                        empty_count += 1
            
            candidate.append((-like_count, -empty_count, x, y))
    
    candidate.sort()
    _, _, r, c = candidate[0]
    table[r][c] = student

score_map = [0, 1, 10, 100, 1000]
total_score = 0

for i in range(N):
    for j in range(N):
        student = table[i][j]

        count = 0
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if table[nx][ny] in likes[student]:
                    count += 1
        total_score += score_map[count]

print(total_score)