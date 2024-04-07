from collections import deque

# 입력받음
N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

# 델타 탐색을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 결과 값으로 사용할 변수. 루프를 돌때마다 1 증가
result = 0

# 조건을 만족한다면 break로 탈출할 루프
while True:

    # 여기서부터 빙산이 몇조각인지 계산하는 로직
    # 동서남북 빙산이 존재하는지 검사하고, 이미 검사한곳은 True로 바꿔줄 것
    visited = [[False] * M for _ in range(N)]

    # 빙산의 개수
    iceberg_count = 0

    # 리스트를 순회하면서
    for i in range(N):
        for j in range(M):

            # 이미 검사한 위치거나, 0이면 continue
            if visited[i][j] == True or iceberg[i][j] == 0:
                continue

            # 검사하지 않은 곳에 빙산이 있다면 BFS로 동서남북 모두 조사
            q = deque()
            # 시작 위치를 큐에 삽입
            q.append((i, j))
            # 빙산의 개수를 하나 증가
            iceberg_count += 1
            # 시작 위치를 True로 바꾸어줌
            visited[i][j] = True

            # BFS를 진행하며 동서남북 조사하지 않은 빙산을 조사
            # 이를 통해 한덩이로 이어진 빙산을 모두 조사 가능
            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and iceberg[nx][ny] != 0:
                        q.append((nx, ny))
                        visited[nx][ny] = True

    # 빙산의 조사가 끝난 후, 2조각 이상이면 탈출
    if iceberg_count >= 2:
        break
    # 빙산이 0개인 경우, 모든 빙산이 2개 이상으로 쪼개지지 않고 끝난 경우
    # 이 때는 result = 0
    if iceberg_count == 0:
        result = 0
        break
    
    # 여기부터 빙산이 녹는 코드 구현
    # 빙산을 한번에 녹이기 위해 리스트 사용
    temp_minus = [[0] * M for _ in range(N)]

    # 리스트를 순회하면서
    for i in range(N):
        for j in range(M):

            # 빙산이 존재한다면 4방향을 조사하고 얼마나 녹는지 temp_minus에 기록
            if iceberg[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and iceberg[nx][ny] < 1:
                        temp_minus[i][j] += 1
    
    # 다시 리스트를 순회하면서 빙산을 녹임
    for i in range(N):
        for j in range(M):
            if temp_minus[i][j] > 0:
                iceberg[i][j] = max(0, iceberg[i][j] - temp_minus[i][j])

    # 한번 루프가 끝나면 햇수를 추가해줌
    result += 1

print(result)