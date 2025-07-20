# [16398] 행성 연결

### **난이도**
골드 4
## **📝문제**
홍익 제국의 중심은 행성 T이다. 제국의 황제 윤석이는 행성 T에서 제국을 효과적으로 통치하기 위해서, N개의 행성 간에 플로우를 설치하려고 한다.

두 행성 간에 플로우를 설치하면 제국의 함선과 무역선들은 한 행성에서 다른 행성으로 무시할 수 있을 만큼 짧은 시간만에 이동할 수 있다. 하지만, 치안을 유지하기 위해서 플로우 내에 제국군을 주둔시켜야 한다.

모든 행성 간에 플로우를 설치하고 플로우 내에 제국군을 주둔하면, 제국의 제정이 악화되기 때문에 황제 윤석이는 제국의 모든 행성을 연결하면서 플로우 관리 비용을 최소한으로 하려 한다.

N개의 행성은 정수 1,…,N으로 표시하고, 행성 i와 행성 j사이의 플로우 관리비용은 Cij이며, i = j인 경우 항상 0이다.

제국의 참모인 당신은 제국의 황제 윤석이를 도와 제국 내 모든 행성을 연결하고, 그 유지비용을 최소화하자. 이때 플로우의 설치비용은 무시하기로 한다.
### **입력**
입력으로 첫 줄에 행성의 수 N (1 ≤ N ≤ 1000)이 주어진다.

두 번째 줄부터 N+1줄까지 각 행성간의 플로우 관리 비용이 N x N 행렬 (Cij), (1 ≤ i, j ≤ N, 1 ≤ Cij ≤ 100,000,000, Cij = Cji, Cii = 0) 로 주어진다.
### **출력**
모든 행성을 연결했을 때, 최소 플로우의 관리비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
3
0 2 3
2 0 1
3 1 0
```

**예제 출력1**

```
3
```

**예제 입력2**

```
5
0 6 8 1 3
6 0 5 7 3
8 5 0 9 4
1 7 9 0 6
3 3 4 6 0
```

**예제 출력2**

```
11
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

visited = [False] * N
pq = []
heappush(pq, (0, 0))

total_cost = 0

while pq:
    cost, now = heappop(pq)

    if visited[now]:
        continue

    visited[now] = True
    total_cost += cost

    for next_node in range(N):
        if not visited[next_node]:
            heappush(pq, (graph[now][next_node], next_node))
    
print(total_cost)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|168872|820|PyPy3|513
#### **📝해설**

**알고리즘**
```
1. 최소 스패닝 트리
```

### **다른 풀이**

```python
from sys import stdin, stdout

N = int(stdin.readline().rstrip())

adjmatrix = []
for _ in range(N):
    adjlist = list(map(int, stdin.readline().split()))
    adjmatrix.append(adjlist)

inf = 500000000 # 임의의 큰 수
visited = [False for _ in range(N)]
visited[0] = True

dist = [adjmatrix[0][i] for i in range(0, N, 1)]
ans = 0
for _ in range(N-1): # prim's algorithm
    minDist = inf
    minIdx = 0
    for i in range(1, N, 1): # visited[0] = True이므로 range에서 제외
        if not visited[i] and dist[i] < minDist:
            minDist = dist[i]
            minIdx = i
    
    ans += minDist
    visited[minIdx] = True
    for i in range(1, N, 1):
        if not visited[i] and adjmatrix[minIdx][i] < dist[i]:
            dist[i] = adjmatrix[minIdx][i]
    
stdout.write(str(ans))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ghdfo5133|120420|296|PyPy3|799
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

# 입력받기
N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 방문 여부 저장
visited = [False] * N

# 최소 힙
pq = []

# 시작 정보 삽입(현재 간선 연결 비용, 현재 노드)
heappush(pq, (0, 0))

# 총 비용
total_cost = 0

# Prim 알고리즘
while pq:
    cost, now = heappop(pq)

    # 이미 방문한 노드라면 건너뜀
    if visited[now]:
        continue
    
    # 현재 노드 방문처리 및 비용 더하기
    visited[now] = True
    total_cost += cost

    # 다음으로 갈 노드를 검사하면서
    for next_node in range(N):

        # 방문하지 않은 곳만 방문
        if not visited[next_node]:

            # 모든 노드를 최소힙에 삽입
            # 최소힙이기 때문에 간선 비용이 작은 노드끼리 연결되게 됨
            heappush(pq, (graph[now][next_node], next_node))
    
print(total_cost)
```