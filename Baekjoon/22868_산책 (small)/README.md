# [22868] 산책 (small)

### **난이도**
골드 3
## **📝문제**
코로나로 인하여 확찐자가 되버려 오늘부터 산책을 하려고 한다. 이를 위해 산책할 경로를 정하려고 한다.

현재 있는 곳 
$S$에서 출발하여 
$S$와 다른 곳인 
$E$를 찍고 다시 
$S$로 돌아오는 경로로 만들려고 한다. 산책을 할 때 이미 갔던 정점을 또 가기 싫어 
$E$에서 
$S$로 올 때 
$S$에서 
$E$로 가는 도중에 방문한 정점을 제외한 다른 정점으로 이동하려고 한다. 또한 산책 거리가 긴 것을 싫어하여 
$S$에서 
$E$로 가는 가장 짧은 거리와 
$E$에서 
$S$로 가는 가장 짧은 거리를 원한다.

정점 
$S$에서 정점 
$E$로 이동할 때, 가장 짧은 거리의 경로가 여러개 나올 수 있다. 그 중, 정점 
$S$에서 정점 
$E$로 이동한 경로를 나열했을 때, 사전순으로 가장 먼저 오는 것을 선택한다.

예를 들어, 정점 1에서 정점 2로 이동한다고 했을 때, 가장 짧은 거리의 경로가 1 4 3 2와 1 3 4 2가 있다고 가정을 해보자. 두 개의 경로중 사전순으로 먼저 오는 것은 1 3 4 2이므로 정점 1에서 정점 2로 가는 최단 경로 중 두 번째 것을 선택한다.

이와 같이 산책 경로를 정할 때, 산책 전체 경로의 거리(
$S$에서 
$E$로 가는 거리 + 
$E$에서 
$S$로 가는 거리)를 구해보자.
### **입력**
첫 번째 줄에는 정점의 개수 
$N$과 두 정점 사이를 잇는 도로의 개수 
$M$이 공백으로 구분되어 주어진다.

두 번째 줄부터 
$M + 1$ 번째 줄까지 정점 
$A$, 
$B$가 공백으로 구분되어 주어진다. 정점 
$A$와 정점 
$B$ 사이의 거리는 항상 1이다. 이때, 정점 
$A$와 정점 
$B$는 양방향으로 이동해도 된다.

정점 
$A$와 정점 
$B$를 잇는 도로는 두개 이상 주어지지 않는다.

 
$M + 2$번째 줄에는 정점 
$S$와 정점 
$E$가 공백으로 구분되어 주어진다.

산책을 할 수 있는 경로가 있는 데이터만 주어진다.
### **출력**
산책의 전체 경로의 길이를 출력한다.
### **예제입출력**

**예제 입력1**

```
4 5
1 2
1 3
2 3
2 4
3 4
1 4
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

S, E = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, N+1):
    edges[i].sort()


visited = [0] * (N+1)
q = deque([(S, 0)])
visited[S] = -1

while q:
    now, dist = q.popleft()
    if now == E:
        break

    for next_node in edges[now]:
        if not visited[next_node]:
            visited[next_node] = now
            q.append((next_node, dist + 1))
    
result = dist

now_node = E
blocked_node = set()

while now_node != S:
    before_node = visited[now_node]
    blocked_node.add(now_node)
    now_node = before_node

visited = [False] * (N+1)
q = deque([(E, 0)])
visited[E] = True

while q:
    now, dist = q.popleft()

    if now == S:
        break

    for next_node in edges[now]:
        if not visited[next_node] and next_node not in blocked_node:
            visited[next_node] = True
            q.append((next_node, dist + 1))

result += dist
print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|39684|128|Python3|1153
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import io
from collections import deque

def s():
    input = io.BufferedReader(io.FileIO(0), 1 << 16).readline

    def bfs(start, goal, adj, banned=None):
        n = len(adj) - 1
        dist, par = [-1]*(n+1), [-1]*(n+1)
        q = deque([start]); dist[start] = 0
        while q:
            u = q.popleft()
            if u == goal: break
            for v in adj[u]:
                if (banned and banned[v]) or dist[v] != -1: continue
                dist[v], par[v] = dist[u] + 1, u
                q.append(v)
        return dist, par

    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b); adj[b].append(a)
    S, E = map(int, input().split())
    for u in range(1, N+1): adj[u].sort()

    d1, p1 = bfs(S, E, adj)
    path, x = [], E
    while x != -1:
        path.append(x)
        if x == S: break
        x = p1[x]
    path.reverse()

    banned = [False]*(N+1)
    for v in path[1:-1]: banned[v] = True

    d2, _ = bfs(E, S, adj, banned)
    print(d1[E] + d2[S])

s()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hanzch|38036|96|Python3|1094
#### **📝해설**

```python
import sys
from collections import deque

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

S, E = map(int, sys.stdin.readline().rstrip().split())

# 사전순으로 방문하기 때문에, 간선 정보들을 모두 오름차순 정렬
for i in range(1, N+1):
    edges[i].sort()

# 방문 여부 및 이전 방문 노드 저장
visited = [0] * (N+1)

# BFS를 위한 queue. (현재 노드, 이동 거리)
q = deque([(S, 0)])

# 시작노드는 이전 방문 노드를 -1로 저장
visited[S] = -1

# BFS
while q:
    now, dist = q.popleft()

    # 도착했다면 종료
    if now == E:
        break

    # 방문 가능한 다음 노드들을 사전순으로 방문
    for next_node in edges[now]:
        if not visited[next_node]:

            # 직전 방문 노드를 저장
            visited[next_node] = now
            q.append((next_node, dist + 1))

# 현재 S -> E까지 이동 거리
result = dist

# 끝에서부터 경로를 추적하며 이미 방문한 노드들은 방문하지 않도록 set로 저장
now_node = E
blocked_node = set()

while now_node != S:
    before_node = visited[now_node]
    blocked_node.add(now_node)
    now_node = before_node

# 이후 E -> S로 다시 BFS
visited = [False] * (N+1)
q = deque([(E, 0)])
visited[E] = True

while q:
    now, dist = q.popleft()

    if now == S:
        break
    
    # 아까와 다르게 이미 방문한 노드는 방문하지 않도록 처리
    for next_node in edges[now]:
        if not visited[next_node] and next_node not in blocked_node:
            visited[next_node] = True
            q.append((next_node, dist + 1))

# E -> S로 이동한 거리 더해줌
result += dist
print(result)
```