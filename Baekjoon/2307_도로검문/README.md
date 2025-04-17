# [2307] 도로검문

### **난이도**
골드 1
## **📝문제**
그림 1은 어떤 도시의 주요 지점과 그 지점들 간의 이동시간을 나타낸 그래프이다. 그래프의 노드는 주요 지점을 나타내고 두 지점을 연결한 도로(에지)에 표시된 수는 그 도로로 이동할 때 걸리는 분 단위의 시간을 나타낸다. 두 지점 a와 b를 연결하는 도로는 도로(a,b)로 표시한다.

[이미지](https://upload.acmicpc.net/9f97f43f-357d-4818-8f7e-47b6a34cc52b/-/preview/)

그림 1

예를 들어 도로(1,2)와 도로(2,3)를 통하여 지점1에서 지점3으로 갈 때 걸리는 시간은 3분이다. 도로는 모두 양방향이라고 가정하므로 도로(a,b)와 도로(b,a)를 지날 때 걸리는 시간은 항상 같다고 한다.

어떤 범죄용의자가 입력 데이터에 표시된 도시로 진입하여 이 도시를 가장 빠른 시간 내에 빠져나가고자 한다. 그런데 이 사실을 알고 있는 경찰이 어떤 하나의 도로(에지)를 선택하여 이 도로에서 검문을 하려고 한다. 따라서 용의자는 이 도로를 피해서 가장 빠르게 도시를 탈출하고자 한다. 이 경우 경찰이 검문을 위하여 선택하는 도로에 따라서 용의자의 가장 빠른 탈출시간은 검문이 없을 때에 비하여 더 늘어날 수 있다.

문제는 도로검문을 통하여 얻을 수 있는 탈출의 최대 지연시간을 계산하는 것이다. 추가설명은 다음과 같다.

1. 두 개의 지점을 직접 연결하는 도로가 있는 경우, 그 도로는 유일하다.
2. 도시의 지점(노드)은 1에서 N번까지 N개의 연속된 정수로 표시된다.
3. 용의자가 도시에 진입하는 지점은 항상 1번이고 도시를 빠져 나가기 위하여 최종적으로 도달해야하는 지점은 항상 N번 지점이다.
4. 용의자는 검문을 피해서 가장 빨리 도시를 빠져나가고자 하고, 경찰은 적절한 도로를 선택하여 이 용이자들의 탈출시간을 최대한 지연시키고자 한다.
5. 각 도시 지점 간을 이동하는 시간은 항상 양의 정수이다.

입력 도시의 도로망에 따라서 경찰이 어떤 도로를 막으면 용의자는 도시를 탈출하지 못할 수도 있다. 이 경우 검문으로 인하여 지연시킬 수 있는 탈출시간은 무한대이다. 이 경우에는 -1을 출력해야 한다.

그림 1에서 볼 때 검문이 없을 경우 용의자가 도시를 탈출하는데 걸리는 시간은 4분이다. 만일 경찰이 도로(4,3)을 막으면 그 탈출시간을 지연시킬 수 없으므로 지연시간은 0이다. 만일 도로(2,3)을 막으면, 용의자들이 가장 빠르게 탈출할 수 있는 시간은 5분이므로 탈출지연시간은 1분이고, 도로(3,6)을 막으면 탈출지연시간은 2분이다.

여러분은 입력 데이터에 표시된 도로망을 읽고, 경찰이 한 도로를 막고 검문함으로써 지연시킬 수 있는 최대시간을 정수로 출력하여야한다. 만일 지연효과가 없으면 0을 출력해야하고, 도시를 빠져나가지 못하게 만들 수 있으면(지연시간이 무한대) -1을 출력해야 한다.
### **입력**
첫 줄에는 지점의 수를 나타내는 정수 N(6 ≤ N ≤ 1000)과 도로의 수 M(6 ≤ M ≤ 5000)이 주어진다. 그 다음 이어 나오는 M개의 각 줄에는 도로(a, b)와 그 통과시간 t가 a b t 로 표시된다. 단 이 경우 a < b 이고 1 ≤ t ≤ 10000이다.
### **출력**
경찰이 하나의 도로를 막음으로써 지연시킬 수 있는 최대 시간을 정수로 출력한다. (단, 그 지연시간이 무한대이면 -1을 출력해야 한다.)
### **예제입출력**

**예제 입력1**

```
6 7
1 2 1
1 4 3
3 6 1
4 5 1
2 3 2
3 4 1
5 6 2
```

**예제 출력1**

```
2
```

**예제 입력2**

```
8 11
1 2 1
1 5 8
1 7 9
2 5 2
3 4 4
3 6 3
3 8 5
4 6 10
4 8 11
5 6 6
5 7 7
```

**예제 출력2**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((t, b))
    edges[b].append((t, a))

dist = [float('inf')] * (N+1)
dist[1] = 0

prev = [-1] * (N+1)

pq = []
heappush(pq, (0, 1))

while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist

        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            prev[next_node] = now_node
            heappush(pq, (new_dist, next_node))
    
min_time = dist[N]

path_edges = []
cur = N
while prev[cur] != -1:
    path_edges.append((prev[cur], cur))
    cur = prev[cur]

max_gap = 0
for case in path_edges:
    dist = [float('inf')] * (N + 1)
    dist[1] = 0

    pq = []
    heappush(pq, (0, 1))

    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for next_dist, next_node in edges[now_node]:
            if (next_node, now_node) == case or (now_node, next_node) == case:
                continue

            new_dist = now_dist + next_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    if dist[N] == float('inf'):
        print(-1)
        exit()

    else:
        max_gap = max(dist[N] - min_time, max_gap)

print(max_gap)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|115672|620|PyPy3|1582
#### **📝해설**

**알고리즘**
```
1. 다익스트라
2. 최단 경로
```

### **다른 풀이**

```python
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


def sol2307():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        distance[u][v] = distance[v][u] = d

    # 다익스트라 최단거리 함수
    def dijkstra(short):
        dp = [INF] * (n + 1)
        q = [(0, 1)]
        dp[1] = 0
        while q:
            if dp[n] <= short:
                return -1

            dst, cur = heappop(q)
            if dst > dp[cur]:
                continue

            for nxt in g[cur]:
                ndst = dst + distance[cur][nxt]
                if ndst < dp[nxt]:
                    dp[nxt] = ndst
                    heappush(q, (ndst, nxt))
        return dp[n]

    # 기존 최단경로를 구하기 위한 다익스트라
    trace = [0] * (n + 1)
    dp = [INF] * (n + 1)
    q = [(0, 1)]
    dp[1] = 0
    while q:
        dst, cur = heappop(q)
        if dst > dp[cur]:
            continue

        for nxt in g[cur]:
            ndst = dst + distance[cur][nxt]
            if ndst < dp[nxt]:
                dp[nxt] = ndst
                trace[nxt] = cur
                heappush(q, (ndst, nxt))

    edges = []
    cur = n
    while trace[cur]:
        edges.append((cur, trace[cur]))
        cur = trace[cur]

    # 도로를 하나씩 봉쇄해가며 가장
    delayed = dp[n]
    for u, v in edges:
        d = distance[u][v]
        distance[u][v] = distance[v][u] = INF
        delayed = max(delayed, dijkstra(delayed))
        distance[u][v] = distance[v][u] = d
        if delayed == INF:
            return -1

    return delayed - dp[n]


if __name__ == '__main__':
    print(sol2307())
    
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
scala0114|124524|544|PyPy3|1861
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((t, b))
    edges[b].append((t, a))

# 거리 정보를 저장할 리스트
dist = [float('inf')] * (N+1)

# 시작점 초기화
dist[1] = 0

# 최단 거리 간선 정보를 저장하기 위한 리스트. 직전 노드의 번호를 저장
prev = [-1] * (N+1)

# 다익스트라 사용을 위한 우선순위 큐
pq = []
heappush(pq, (0, 1))

# 다익스트라 알고리즘
while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist

        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            # 이전 노드의 인덱스를 저장하면서 최단 경로를 파악할 수 있음
            prev[next_node] = now_node
            heappush(pq, (new_dist, next_node))

# 도로를 막지 않았을 때 최단 거리
min_time = dist[N]

# 지나온 간선의 정보를 저장할 리스트
path_edges = []
cur = N

# 역추적을 통해 지나온 경로를 저장
while prev[cur] != -1:
    path_edges.append((prev[cur], cur))
    cur = prev[cur]

# 도로를 막았을 때 최대로 얻을 수 있는 효과 변수
max_gap = 0

# 최단 경로 중에서 하나씩 도로를 막으면서 최대 효율 검사
for case in path_edges:
    dist = [float('inf')] * (N + 1)
    dist[1] = 0

    pq = []
    heappush(pq, (0, 1))

    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for next_dist, next_node in edges[now_node]:
            if (next_node, now_node) == case or (now_node, next_node) == case:
                continue

            new_dist = now_dist + next_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    # 도달 할 수 없는 경우가 생긴다면 -1을 출력하고 바로 종료
    if dist[N] == float('inf'):
        print(-1)
        exit()

    # 최대 효율을 갱신
    else:
        max_gap = max(dist[N] - min_time, max_gap)

print(max_gap)
```