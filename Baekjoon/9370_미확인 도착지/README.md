# [9370] 미확인 도착지

### **난이도**
골드 2
## **📝문제**
(취익)B100 요원, 요란한 옷차림을 한 서커스 예술가 한 쌍이 한 도시의 거리들을 이동하고 있다. 너의 임무는 그들이 어디로 가고 있는지 알아내는 것이다. 우리가 알아낸 것은 그들이 s지점에서 출발했다는 것, 그리고 목적지 후보들 중 하나가 그들의 목적지라는 것이다. 그들이 급한 상황이기 때문에 목적지까지 우회하지 않고 최단거리로 갈 것이라 확신한다. 이상이다. (취익)

어휴! (요란한 옷차림을 했을지도 모를) 듀오가 어디에도 보이지 않는다. 다행히도 당신은 후각이 개만큼 뛰어나다. 이 후각으로 그들이 g와 h 교차로 사이에 있는 도로를 지나갔다는 것을 알아냈다.

이 듀오는 대체 어디로 가고 있는 것일까?

![이미지](https://www.acmicpc.net/upload/images/destination.png)

예제 입력의 두 번째 케이스를 시각화한 것이다. 이 듀오는 회색 원에서 두 검은 원 중 하나로 가고 있고 점선으로 표시된 도로에서 냄새를 맡았다. 따라서 그들은 6으로 향하고 있다.
### **입력**
첫 번째 줄에는 테스트 케이스의 T(1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스마다

- 첫 번째 줄에 3개의 정수 n, m, t (2 ≤ n ≤ 2 000, 1 ≤ m ≤ 50 000 and 1 ≤ t ≤ 100)가 주어진다. 각각 교차로, 도로, 목적지 후보의 개수이다.
- 두 번째 줄에 3개의 정수 s, g, h (1 ≤ s, g, h ≤ n)가 주어진다. s는 예술가들의 출발지이고, g, h는 문제 설명에 나와 있다. (g ≠ h)
- 그 다음 m개의 각 줄마다 3개의 정수 a, b, d (1 ≤ a < b ≤ n and 1 ≤ d ≤ 1 000)가 주어진다. a와 b 사이에 길이 d의 양방향 도로가 있다는 뜻이다.
- 그 다음 t개의 각 줄마다 정수 x가 주어지는데, t개의 목적지 후보들을 의미한다. 이 t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않다.

교차로 사이에는 도로가 많아봐야 1개이다. m개의 줄 중에서 g와 h 사이의 도로를 나타낸 것이 존재한다. 또한 이 도로는 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부이다.
### **출력**
테스트 케이스마다

입력에서 주어진 목적지 후보들 중 불가능한 경우들을 제외한 목적지들을 공백으로 분리시킨 오름차순의 정수들로 출력한다.
### **예제입출력**

**예제 입력1**

```
2
5 4 2
1 2 3
1 2 6
2 3 2
3 4 4
3 5 3
5
4
6 9 2
2 3 1
1 2 1
1 3 3
2 4 4
2 5 5
3 4 3
3 6 2
4 5 4
4 6 3
5 6 7
5
6
```

**예제 출력1**

```
4 5
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

def dijkstra(start, n, graph):
    dist = [int(21e8)] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, now = heappop(heap)
        if cost > dist[now]:
            continue
        for weight, nxt in graph[now]:
            if dist[nxt] > cost + weight:
                dist[nxt] = cost + weight
                heappush(heap, (cost + weight, nxt))
    return dist

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N, M, T = map(int, sys.stdin.readline().rstrip().split())
    S, G, H = map(int, sys.stdin.readline().rstrip().split())
    edges = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, d = map(int, sys.stdin.readline().rstrip().split())
        edges[a].append((d, b))
        edges[b].append((d, a))
    
    destinations = []
    for _ in range(T):
        x = int(sys.stdin.readline().rstrip())
        destinations.append(x)
    
    dist_s = dijkstra(S, N, edges)
    dist_g = dijkstra(G, N, edges)
    dist_h = dijkstra(H, N, edges)

    answer = []

    for destination in destinations:
        route1 = dist_s[G] + dist_g[H] + dist_h[destination]
        route2 = dist_s[H] + dist_h[G] + dist_g[destination]

        if dist_s[destination] == route1 or dist_s[destination] == route2:
            answer.append(destination)
    
    print(" ".join(map(str, sorted(answer))))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|121180|264|PyPy3|1411
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

### **다른 풀이**

```python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = float('inf')

def dijkstra(graph, start, cnt):
    cost = [INF] * cnt
    cost[start] = 0
    cur = [(0, start)]

    while cur:
        p, x = heappop(cur)
        if p > cost[x]: continue

        for to, c in graph[x]:
            if cost[x] + c < cost[to]:
                cost[to] = cost[x] + c
                heappush(cur, (cost[to], to))
    
    return cost

def solution():
    N, M, T = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, d = map(int, input().split())
        graph[a].append((b, d << 1))
        graph[b].append((a, d << 1))
    
    f1 = next(filter(lambda k: graph[g][k][0]==h, range(len(graph[g]))))
    f2 = next(filter(lambda k: graph[h][k][0]==g, range(len(graph[h]))))
    graph[g][f1] = (graph[g][f1][0], graph[g][f1][1] - 1)
    graph[h][f2] = (graph[h][f2][0], graph[h][f2][1] - 1)

    dest = tuple(int(input()) for _ in range(T))
    cost = dijkstra(graph, s, N+1)
    
    return ' '.join(list(map(str, sorted([ i for i in dest if cost[i] != INF and cost[i] & 1 ]))))

print('\n'.join([solution() for _ in range(int(input()))]))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
amgkd9|46532|224|Python3|1240
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

# 다익스트라 탐색을 하는 함수
def dijkstra(start, n, graph): # 시작점, 교차로의 개수, 그래프

    # start에서 시작했을 때, 각 노드까지의 최단거리
    dist = [int(21e8)] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, now = heappop(heap)
        if cost > dist[now]:
            continue
        for weight, nxt in graph[now]:
            if dist[nxt] > cost + weight:
                dist[nxt] = cost + weight
                heappush(heap, (cost + weight, nxt))
    
    # 각 노드까지의 최단거리를 리턴
    return dist

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    # 입력받기
    N, M, T = map(int, sys.stdin.readline().rstrip().split())
    S, G, H = map(int, sys.stdin.readline().rstrip().split())
    edges = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, d = map(int, sys.stdin.readline().rstrip().split())
        edges[a].append((d, b))
        edges[b].append((d, a))
    
    destinations = []
    for _ in range(T):
        x = int(sys.stdin.readline().rstrip())
        destinations.append(x)
    
    # 각각 S, G, H에서 시작한 경우 각 노드까지의 최단거리를 저장
    dist_s = dijkstra(S, N, edges)
    dist_g = dijkstra(G, N, edges)
    dist_h = dijkstra(H, N, edges)

    answer = []

    # 도착 후보지들을 검사하면서
    for destination in destinations:

        # s에서 출발해서 G, G에서 출발해서 H, H에서 출발해서 도착지까지의 거리를 구함
        route1 = dist_s[G] + dist_g[H] + dist_h[destination]
        # H를 먼저 방문하는 경우도 고려
        route2 = dist_s[H] + dist_h[G] + dist_g[destination]

        # 총 거리 합이 둘 중 하나라면
        if dist_s[destination] == route1 or dist_s[destination] == route2:

            # 정답으로 저장
            answer.append(destination)
    
    print(" ".join(map(str, sorted(answer))))
```