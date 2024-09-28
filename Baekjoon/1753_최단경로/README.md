# [1753] 최단경로

### **난이도**
골드4
## **📝문제**
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
### **입력**
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
### **출력**
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
### **예제입출력**

**예제 입력1**

```
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
```

**예제 출력1**

```
0
2
3
7
INF
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

V, E = map(int, input().split())
start_node = int(input())

edges = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, length = map(int, sys.stdin.readline().rstrip().split())
    edges[start].append((length, end))

dist = [float('inf')] * (V+1)
dist[start_node] = 0

pq = []
heappush(pq, (0, start_node))

while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist
        if dist[next_node] > new_dist:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

for i in range(1, V+1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|136008|388|PyPy3|789
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

#### **📝해설**

```python
import sys
from heapq import heappush, heappop

V, E = map(int, input().split())
start_node = int(input())

edges = [[] for _ in range(V+1)]
# 간선 정보 삽입
for _ in range(E):
    start, end, length = map(int, sys.stdin.readline().rstrip().split())
    edges[start].append((length, end))

# 최단거리를 저장할 리스트
dist = [float('inf')] * (V+1)
dist[start_node] = 0

# 다익스트라 시작을 위한 우선순위큐 선언
pq = []
heappush(pq, (0, start_node))

# 다익스트라 진행
while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist
        if dist[next_node] > new_dist:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

for i in range(1, V+1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])
```