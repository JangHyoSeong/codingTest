# [17835] 면접보는 승범이네

### **난이도**
골드 2
## **📝문제**
마포구에는 모든 대학생이 입사를 희망하는 굴지의 대기업 ㈜승범이네 본사가 자리를 잡고 있다. 승범이는 ㈜승범이네의 사장인데, 일을 못 하는 직원들에게 화가 난 나머지 전 직원을 해고하고 신입사원을 뽑으려 한다. 1차 서류전형이 끝난 뒤 합격자들은 면접을 준비하게 되었다.

면접자들은 서로 다른 N개의 도시에 거주한다. 승범이는 면접자들의 편의를 위해 거주 중인 N개 도시 중 K개의 도시에 면접장을 배치했다. 도시끼리는 단방향 도로로 연결되며, 거리는 서로 다를 수 있다. 어떤 두 도시 사이에는 도로가 없을 수도, 여러 개가 있을 수도 있다. 또한 어떤 도시에서든 적어도 하나의 면접장까지 갈 수 있는 경로가 항상 존재한다.

모든 면접자는 본인의 도시에서 출발하여 가장 가까운 면접장으로 찾아갈 예정이다. 즉, 아래에서 언급되는 '면접장까지의 거리'란 그 도시에서 도달 가능한 가장 가까운 면접장까지의 최단 거리를 뜻한다.

속초 출신 승범이는 지방의 서러움을 알기에 각 도시에서 면접장까지의 거리 중, 그 거리가 가장 먼 도시에서 오는 면접자에게 교통비를 주려고 한다.

승범이를 위해 면접장까지의 거리가 가장 먼 도시와 그 거리를 구해보도록 하자.
### **입력**
첫째 줄에 도시의 수 N(2 ≤ N ≤ 100,000), 도로의 수 M(1 ≤ M ≤ 500,000), 면접장의 수 K(1 ≤ K ≤ N)가 공백을 두고 주어진다. 도시는 1번부터 N번까지의 고유한 번호가 매겨진다.

다음 M개의 줄에 걸쳐 한 줄마다 도시의 번호 U, V(U ≠ V)와 도로의 길이 C(1 ≤ C ≤ 100,000)가 공백을 두고 순서대로 주어진다. 이는 도시 U에서 V로 갈 수 있는 도로가 존재하고, 그 거리가 C라는 뜻이다.

마지막 줄에 면접장이 배치된 도시의 번호 K개가 공백을 두고 주어진다.
### **출력**
첫째 줄에 면접장까지 거리가 가장 먼 도시의 번호를 출력한다. 만약 그런 도시가 여러 곳이면 가장 작은 번호를 출력한다.

둘째 줄에 해당 도시에서 면접장까지의 거리를 출력한다.
### **예제입출력**

**예제 입력1**

```
6 10 2
2 6 2
1 4 1
6 1 5
2 5 1
5 1 4
4 5 6
6 2 3
3 5 1
3 1 1
5 2 2
1 2
```

**예제 출력1**

```
4
8
```

**예제 입력2**

```
10 20 5
4 1 18
6 1 7
2 4 1
5 6 18
7 6 10
10 6 9
3 2 4
8 3 10
9 8 15
7 1 12
10 7 1
8 1 3
6 5 19
2 9 10
7 2 4
10 3 20
7 10 14
5 7 12
8 4 10
2 5 8
1 8 4 6 7
```

**예제 출력2**

```
9
15
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

INF = float('inf')

N, M, K = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, c = map(int, sys.stdin.readline().rstrip().split())
    edges[v].append((c, u))

cities = list(map(int, sys.stdin.readline().rstrip().split()))

pq = []
dist = [INF] * (N+1)
for city in cities:
    dist[city] = 0
    heappush(pq, (0, city))

while pq:
    cost, now = heappop(pq)
    if cost > dist[now]:
        continue

    for next_cost, next_city in edges[now]:
        new_cost = next_cost + cost

        if dist[next_city] > new_cost:
            dist[next_city] = new_cost
            heappush(pq, (new_cost, next_city))

max_dist = -1
city_num = -1

for i in range(1, N+1):
    if dist[i] > max_dist:
        max_dist = dist[i]
        city_num = i

print(city_num)
print(max_dist)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|155916|960|PyPy3|880
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

### **다른 풀이**

```python
import io, os
import heapq as hq
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
INF = 1<<40
def main():
    N, M, K = map(int, input().split())
    graph = [{} for _ in range(N + 1)]
    dist = [INF] * (N + 1)
    for _ in range(M):
        u, v, c = map(int, input().split())
        if c0:=(graph[v].get(u)) is not None and c0 <= c:
            continue
        graph[v][u] = c
    marked = [*map(int, input().split())]
    que = []
    for m in marked:
        dist[m] = 0
        que.append((0, m))
    ans = 0
    while que:
        d, u = hq.heappop(que)
        if d > dist[u]:
            continue
        ans = d
        for v, w in graph[u].items():
            if d + w < dist[v]:
                dist[v] = d + w
                hq.heappush(que, (d + w, v))
    for i, d in enumerate(dist):
        if d == ans:
            print(i)
            print(ans)
            return
main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
minskai|175856|676|PyPy3|906
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

# 임의의 큰 값
INF = float('inf')

N, M, K = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

# 간선 정보를 역방향으로 저장(도착점에서부터 역추적)
for _ in range(M):
    u, v, c = map(int, sys.stdin.readline().rstrip().split())
    edges[v].append((c, u))

# 도착지점들
cities = list(map(int, sys.stdin.readline().rstrip().split()))

# 다익스트라를 위한 PQ
pq = []

# 도착지점들까지의 거리
dist = [INF] * (N+1)
for city in cities:
    dist[city] = 0

    # 도착점을 모두 우선순위 큐에 삽입
    heappush(pq, (0, city))

# 다익스트라 시작
while pq:
    cost, now = heappop(pq)
    if cost > dist[now]:
        continue

    for next_cost, next_city in edges[now]:
        new_cost = next_cost + cost

        if dist[next_city] > new_cost:
            dist[next_city] = new_cost
            heappush(pq, (new_cost, next_city))

# 최대 거리, 그때의 도시 번호
max_dist = -1
city_num = -1

for i in range(1, N+1):
    if dist[i] > max_dist:
        max_dist = dist[i]
        city_num = i

print(city_num)
print(max_dist)
```