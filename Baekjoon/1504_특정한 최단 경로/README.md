# [1504] 특정한 최단 경로

### **난이도**
골드 4
## **📝문제**
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.


### **입력**
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.
### **출력**
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
```

**예제 출력1**

```
7
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappop, heappush

N, E = map(int, input().split())

edges = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, graph, n):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        now_dist, now_node = heappop(pq)

        if distance[now_node] < now_dist:
            continue

        for next_node, next_dist in graph[now_node]:
            new_dist = next_dist + now_dist

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    return distance

dist_from_1 = dijkstra(1, edges, N)
dist_from_v1 = dijkstra(v1, edges, N)
dist_from_v2 = dijkstra(v2, edges, N)

path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

result = min(path1, path2)
print(result if result < float('inf') else -1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|128436|300|PyPy3|1104
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

#### **📝해설**

```python
import sys
from heapq import heappop, heappush

N, E = map(int, input().split())

edges = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

v1, v2 = map(int, input().split())

# 다익스트라 함수
def dijkstra(start, graph, n):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        now_dist, now_node = heappop(pq)

        if distance[now_node] < now_dist:
            continue

        for next_node, next_dist in graph[now_node]:
            new_dist = next_dist + now_dist

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    return distance


# 1에서 시작한경우, v1에서 시작한경우, v2에서 시작한경우를 모두 최단거리를 구함
dist_from_1 = dijkstra(1, edges, N)
dist_from_v1 = dijkstra(v1, edges, N)
dist_from_v2 = dijkstra(v2, edges, N)


# 1에서 v1까지가고, v1에서 v2까지가고, v2에서 N까지 간 길이
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]

# 1 -> v2 -> v1 -> N 의 길이
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

# 최소값을 출력
result = min(path1, path2)
print(result if result < float('inf') else -1)
```