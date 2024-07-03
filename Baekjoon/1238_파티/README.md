# [1238] 파티

### **난이도**
골드 3
## **📝문제**
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다. 두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다. 시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.
### **출력**
첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
```

**예제 출력1**

```
10
```

### **출처**
Olympiad > USA Computing Olympiad > 2006-2007 Season > USACO February 2007 Contest > Silver 3번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappop, heappush
INF = 21e8

def dijkstra(start, target):

    distance = [INF] * (N+1)
    distance[start] = 0
    
    pq = []
    heappush(pq, (0, start))
    
    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for to in graph[now]:
            next_node, next_dist = to[0], to[1]
            new_dist = next_dist + dist
            
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return distance[target]

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

max_time = 0
for i in range(1, N+1):
    temp_time_go = dijkstra(i, X)
    temp_time_back = dijkstra(X, i)

    max_time = max(max_time, temp_time_back + temp_time_go)

print(max_time)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34212|1848|Python3|952
#### **📝해설**

**알고리즘**
```
1. 다이스트라
```

### **다른 풀이**

```python
import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())
n_routes = [[] for _ in range(n+1)]
r_routes = [[] for _ in range(n+1)]
n_visit = [-1] * (n+1)
r_visit = [-1] * (n+1)

for i in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    n_routes[s].append((w, e))
    r_routes[e].append((w, s))

hq = n_routes[x]
n_visit[x] = 0
heapq.heapify(hq)

while hq:
    w, v = heapq.heappop(hq)
    if n_visit[v] != -1:
        continue
    n_visit[v] = w
    for ww, vv in n_routes[v]:
        if n_visit[vv] == -1:
            heapq.heappush(hq, (ww+w, vv))


hq = r_routes[x]
r_visit[x] = 0
heapq.heapify(hq)
while hq:
    w, v = heapq.heappop(hq)
    if r_visit[v] != -1:
        continue
    r_visit[v] = w
    for ww, vv in r_routes[v]:
        if r_visit[vv] == -1:
            heapq.heappush(hq, (ww+w, vv))

min_d = r_visit[1] + n_visit[1]
for i in range(2, n+1, 1):
    min_d = max(min_d, r_visit[i] + n_visit[i])
print(min_d)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20230660|34236|52|Python3|959
#### **📝해설**

```python
from heapq import heappop, heappush
INF = 21e8

def dijkstra(start, target):
    # 목표지점까지 최단거리를 찾는 다이스트라 함수
    distance = [INF] * (N+1)
    distance[start] = 0
    
    pq = []
    heappush(pq, (0, start))
    
    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for to in graph[now]:
            next_node, next_dist = to[0], to[1]
            new_dist = next_dist + dist
            
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return distance[target]

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 간선 정보를 저장
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

max_time = 0
# 모든 노드에서부터 X노드를 다녀오는데 걸리는 거리를 측정
for i in range(1, N+1):
    temp_time_go = dijkstra(i, X)
    temp_time_back = dijkstra(X, i)

    max_time = max(max_time, temp_time_back + temp_time_go)

print(max_time)
```