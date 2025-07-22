# [24445] 알고리즘 수업 - 너비 우선 탐색 2

### **난이도**
실버 2
## **📝문제**
오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 내림차순으로 방문한다.

```
bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    for each v ∈ V - {R}
        visited[v] <- NO;
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while (Q ≠ ∅) {
        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
            if (visited[v] = NO) then {
                visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
                enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
            }
    }
}
```
### **입력**
첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.
### **출력**
첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. i번째 줄에는 정점 i의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 5 1
1 4
1 2
2 3
2 4
3 4
```

**예제 출력1**

```
1
3
4
2
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1, N+1):
    edges[i].sort(reverse=True)

q = deque([R])
visited = [0] * (N + 1)
visited[R] = 1

count = 1
while q:
    now = q.popleft()

    for next_node in edges[now]:
        if not visited[next_node]:
            count += 1
            q.append(next_node)
            visited[next_node] = count

for i in range(1, N+1):
    print(visited[i])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|129572|336|PyPy3|621
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
import sys
from collections import deque

# 입력받기
N, M, R = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

# 내림차순으로 정렬
for i in range(1, N+1):
    edges[i].sort(reverse=True)

# BFS를 위한 초기 정보 입력
q = deque([R])
visited = [0] * (N + 1)
visited[R] = 1

# 몇번째 방문한 노드인지 저장하기 위한 변수
count = 1
while q:
    now = q.popleft()

    # 다음 노드를 방문하면서
    for next_node in edges[now]:
        if not visited[next_node]:

            # 몇번째 방문인지 기록
            count += 1
            q.append(next_node)
            visited[next_node] = count

for i in range(1, N+1):
    print(visited[i])
```