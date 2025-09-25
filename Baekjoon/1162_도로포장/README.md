# [1162] 도로포장

### **난이도**
플래티넘 1
## **📝문제**
준영이는 매일 서울에서 포천까지 출퇴근을 한다. 하지만 잠이 많은 준영이는 늦잠을 자 포천에 늦게 도착하기 일쑤다. 돈이 많은 준영이는 고민 끝에 K개의 도로를 포장하여 서울에서 포천까지 가는 시간을 단축하려 한다.

문제는 N개의 도시가 주어지고 그 사이 도로와 이 도로를 통과할 때 걸리는 시간이 주어졌을 때 최소 시간이 걸리도록 하는 K개의 이하의 도로를 포장하는 것이다. 도로는 이미 있는 도로만 포장할 수 있고, 포장하게 되면 도로를 지나는데 걸리는 시간이 0이 된다. 또한 편의상 서울은 1번 도시, 포천은 N번 도시라 하고 1번에서 N번까지 항상 갈 수 있는 데이터만 주어진다.
### **입력**
첫 줄에는 도시의 수 N(1 ≤ N ≤ 10,000)과 도로의 수 M(1 ≤ M ≤ 50,000)과 포장할 도로의 수 K(1 ≤ K ≤ 20)가 공백으로 구분되어 주어진다. M개의 줄에 대해 도로가 연결하는 두 도시와 도로를 통과하는데 걸리는 시간이 주어진다. 도로들은 양방향 도로이며, 걸리는 시간은 1,000,000보다 작거나 같은 자연수이다.
### **출력**
첫 줄에 K개 이하의 도로를 포장하여 얻을 수 있는 최소 시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 4 1
1 2 10
2 4 10
1 3 1
3 4 100
```

**예제 출력1**

```
1
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappush, heappop
import sys

INF = float('inf')

N, M, K = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, time = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((time, b))
    edges[b].append((time, a))

dist = [[INF] * (K + 1) for _ in range(N+1)]
dist[1][0] = 0

# 거리, 노드, K
pq = [(0, 1, 0)]
while pq:
    now_dist, now_node, k = heappop(pq)

    if now_dist > dist[now_node][k]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist
        if new_dist < dist[next_node][k]:
            dist[next_node][k] = new_dist
            heappush(pq, (new_dist, next_node, k))
        
        if k + 1 <= K and now_dist < dist[next_node][k+1]:
            dist[next_node][k+1] = now_dist
            heappush(pq, (now_dist, next_node, k+1))

print(min(dist[N]))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|185536|1304|PyPy3|919
#### **📝해설**

**알고리즘**
```
1. DP
2. 다익스트라
```

### **다른 풀이**

```python
import sys
import heapq
input = sys.stdin.readline

V, E, K = map(int, input().split())
graph = [[] for _ in range(V + 1)]
res = float("inf")

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dijkstra(start):
    weight = [[float("inf")] * (V + 1) for _ in range(K + 1)]
    heap = []
    weight[K][start] = 0
    heapq.heappush(heap, (0, start, K))
    while heap:
        dist, node, road = heapq.heappop(heap)
        if dist > weight[road][node]:
            continue

        for next in graph[node]:
            cost = dist + next[1]
            if cost < weight[road][next[0]]:
                weight[road][next[0]] = cost
                heapq.heappush(heap, (cost, next[0], road))

            if road > 0:
                cost = dist
                if cost < weight[road - 1][next[0]]:
                    weight[road - 1][next[0]] = cost
                    heapq.heappush(heap, (cost, next[0], road - 1))

    return weight

lst = dijkstra(1)

for i in range(K + 1):
    res = min(res, lst[i][V])

print(res)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ioprt123|55080|900|Python3|1093
#### **📝해설**

```python
from heapq import heappush, heappop
import sys

INF = float('inf')

# 입력받기
N, M, K = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

# 간선정보 저장
for _ in range(M):
    a, b, time = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((time, b))
    edges[b].append((time, a))

# 도로 포장한 횟수까지 이차원 리스트로 만듦
dist = [[INF] * (K + 1) for _ in range(N+1)]

# 시작점 초기화
dist[1][0] = 0

# 거리, 노드, K
pq = [(0, 1, 0)]

# 다익스트라
while pq:
    now_dist, now_node, k = heappop(pq)

    # 이미 최단거리가 아닌 경우 고려하지 않음
    if now_dist > dist[now_node][k]:
        continue

    # 다음 노드를 탐색하면서
    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist

        # 거리가 더 짧다면 이동
        if new_dist < dist[next_node][k]:
            dist[next_node][k] = new_dist
            heappush(pq, (new_dist, next_node, k))
        
        # 도로를 포장하고, 거리가 더 짧다면 이동
        if k + 1 <= K and now_dist < dist[next_node][k+1]:
            dist[next_node][k+1] = now_dist
            heappush(pq, (now_dist, next_node, k+1))

print(min(dist[N]))
```