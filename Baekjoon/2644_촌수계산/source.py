from collections import deque

N = int(input())
start, end = map(int, input().split())
M = int(input())

# 데이터 형태를 족보(트리)라고 생각하고 간선의 정보를 입력함
arr = [[] for _ in range(N+1)]
for i in range(M):
    # 무방향 그래프
    child, parent = map(int, input().split())
    arr[parent].append(child)
    arr[child].append(parent)

# 방문 여부를 표시하는 리스트
visited = [False] * (N+1)

# q에 시작위치를 넣고 BFS 탐색 시작
q = deque([[start, 0]])
visited[start] = True

while q:
    # 현재 위치를 q에서 pop
    now, count = q.popleft()
    
    # 만약 도착했다면 break
    if now == end:
        break
    
    # 현재 노드에서 갈 수 있는 모든 노드를 방문
    for next in arr[now]:
        if not visited[next]:
            # 다음 노드의 번호와 이동 횟수를 queue에 삽입
            q.append([next, count+1])
            # 방문 처리
            visited[next] = True

# 도착노드에 방문하지 않았다면 연결되지 않은것
if not visited[end]:
    print(-1)
# 도착 노드에 방문했다면 이동 횟수 출력
else:
    print(count)