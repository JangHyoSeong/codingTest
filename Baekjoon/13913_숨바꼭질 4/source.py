from collections import deque

N, K = map(int,input().split())

# 방문 여부와, 방문 시 몇번째 이동인지 기록할 리스트
visited = [None] * 100001

# 몇번에서 왔는지 기록할 리스트
# 예를들어 5에서 10으로 이동한 경우 footpirnts[10] = 5
footprints = [None] * 100001

# BFS의 시작 세팅
q = deque()
q.append(N)
visited[N] = 0

# BFS 실행
while q:
    N = q.popleft()

    # 목표지점에 도착했다면 종료
    if N == K:
        break

    # N*2, N+1, N-1을 진행
    for new_N in [N*2, N+1, N-1]:
        # 범위를 벗어나지 않고
        if 0 <= new_N < 100001:

            # 방문한 적 없다면
            if visited[new_N] is None:
                # q에 삽입, visited를 현재 이동 횟수로 설정, footprints에 발자취 남김
                q.append(new_N)
                visited[new_N] = visited[N] + 1
                footprints[new_N] = N

# visited[K]는 몇 번 이동했는지 기록되어 있음
print(visited[K])

# 어떻게 움직였는지 기록할 리스트
# 움직임의 역순으로 기록됨
result = [K]

# 발자취를 거슬러 올라가면서 result에 기록
for i in range(visited[K]):
    result.append(footprints[result[-1]])

# 출력
for i in range(len(result)-1, -1, -1):
    print(result[i], end=" ")