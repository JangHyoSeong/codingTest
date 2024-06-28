# 출퇴근길

### **난이도**
Lv 3
## **📝문제**
https://softeer.ai/practice/6248

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

def bfs(start, edges, visited, stop_at=None):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        if stop_at is not None and now == stop_at:
            continue
        for next in edges[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

N, M = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
edges_re = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    edges[start].append(end)
    edges_re[end].append(start)

S, T = map(int, sys.stdin.readline().split())

visited_StoT = [False] * (N+1)
bfs(S, edges, visited_StoT, stop_at=T)

visited_StoT_re = [False] * (N+1)
bfs(T, edges_re, visited_StoT_re)

visited_TtoS = [False] * (N+1)
bfs(T, edges, visited_TtoS, stop_at=S)

visited_TtoS_re = [False] * (N+1)
bfs(S, edges_re, visited_TtoS_re)

count = 0
for i in range(1, N+1):
    if i == S or i == T:
        continue
        
    if visited_StoT[i] and visited_StoT_re[i] and visited_TtoS[i] and visited_TtoS_re[i]:
        count += 1

print(count)
```

#### **📝해설**

**알고리즘**
```
1. BFS
2. 역 그래프 탐색
```

#### **📝해설**

```python
import sys
from collections import deque

def bfs(start, edges, visited, stop_at=None):
    # BFS를 위한 함수.
    # 각 매개변수는 시작점, 간선정보, 방문여부를 저장할 리스트, 도착점이다.

    # bfs를 시작할 위치를 queue에 삽입
    q = deque([start])

    # 시작점을 방문처리
    visited[start] = True

    # q가 빌 때까지
    while q:

        # 현재위치
        now = q.popleft()

        # 역방향 그래프의 경우, 도착점에 여러번 도착해도 됨(도착점이 S)
        # 정방향 그래프의 경우, 도착점에 도착하면 끝. 따라서 그 경우 다음 노드로 이동하지 않아야하기에 continue
        if stop_at is not None and now == stop_at:
            continue

        # 현재 위치에서 방문하지 않고, 갈 수 있는 모든 정점에 방문
        for next in edges[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

# 입력받음
N, M = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
edges_re = [[] for _ in range(N+1)]

# 간선 정보를 저장하고, 시작점과 도착점을 바꾼 역방향 간선정보도 저장
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    edges[start].append(end)
    edges_re[end].append(start)

S, T = map(int, sys.stdin.readline().split())

# S에서 BFS를 통해 도달할 수 있는 모든 지점 저장
visited_StoT = [False] * (N+1)
bfs(S, edges, visited_StoT, stop_at=T)

# T에서 역방향 간선 정보를 통해 BFS를 통해 도달할 수 있는 모든 지점 저장
visited_StoT_re = [False] * (N+1)
bfs(T, edges_re, visited_StoT_re)
# 이 두 지점의 교집합이 S에서 T로 이동할 때 방문하는 모든 정점 정보가 됨

# 반대의 경우도 동일
visited_TtoS = [False] * (N+1)
bfs(T, edges, visited_TtoS, stop_at=S)

visited_TtoS_re = [False] * (N+1)
bfs(S, edges_re, visited_TtoS_re)

count = 0
for i in range(1, N+1):
    # 시작점과 끝점은 방문 정점에서 제외
    if i == S or i == T:
        continue
    
    # 모든 visited가 방문한 곳이 문제에서 찾는 정답
    if visited_StoT[i] and visited_StoT_re[i] and visited_TtoS[i] and visited_TtoS_re[i]:
        count += 1

print(count)
```

### **🔖정리**

1. 역 그래프의 사용 이유와, 어떤 상황에서 사용해야 하는 지 알 수 있었다.
2. 한 정점에서 도달할 수 있는 정점들을 구할 때, 역그래프를 사용한다.