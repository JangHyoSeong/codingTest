# [22865] 가장 먼 곳

### **난이도**
골드 4
## **📝문제**
$N$개의 땅 중에서 한 곳에 자취를 하려고 집을 알아보고 있다. 세 명의 친구 
$A$, 
$B$, 
$C$가 있는데 이 친구들이 살고 있는 집으로부터 가장 먼 곳에 집을 구하려고 한다.

이때, 가장 먼 곳은 선택할 집에서 거리가 가장 가까운 친구의 집까지의 거리를 기준으로 거리가 가장 먼 곳을 의미한다.

예를 들어, 
$X$ 위치에 있는 집에서 친구 
$A$, 
$B$, 
$C$의 집까지의 거리가 각각 3, 5, 4이라 가정하고 
$Y$ 위치에 있는 집에서 친구 
$A$, 
$B$, 
$C$의 집까지의 거리가 각각 5, 7, 2라고 하자.

이때, 친구들의 집으로부터 땅 
$X$와 땅 
$Y$ 중 더 먼 곳은 땅 
$X$이다. 왜냐하면 
$X$에서 가장 가까운 친구의 집까지의 거리는 3이고, 
$Y$에서는 
$2$이기 때문이다.

친구들이 살고 있는 집으로부터 가장 먼 곳을 구해보자.
### **입력**
첫번째 줄에 자취할 땅 후보의 개수 
$N$이 주어진다.

2번째 줄에는 친구 
$A$, 
$B$, 
$C$가 사는 위치가 공백으로 구분되어 주어진다. 이때 친구들은 
$N$개의 땅 중 하나에 사는 것이 보장된다. (같은 위치에서 살 수 있다.)

3번째 줄에는 땅과 땅 사이를 잇는 도로의 개수 
$M$이 주어진다.

그 다음줄부터 
$M + 3$번째 줄까지 땅 
$D$, 땅 
$E$, 땅 
$D$와 땅 
$E$와 사이를 연결하는 도로의 길이 
$L$이 공백으로 구분되어 주어진다. 이 도로는 양뱡항 통행이 가능하다.
### **출력**
친구들이 살고 있는 집으로부터 가장 먼 곳의 땅 번호를 출력한다. 만약 가장 먼 곳이 여러 곳이라면 번호가 가장 작은 땅의 번호를 출력한다.
### **예제입출력**

**예제 입력1**

```
6
1 2 5
8
1 2 1
2 3 4
1 4 2
2 5 3
1 6 5
5 6 2
3 4 2
4 5 6
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

INF = int(21e8)

N = int(sys.stdin.readline().rstrip())
A, B, C = map(int, sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    D, E, length = map(int, sys.stdin.readline().rstrip().split())
    edges[D].append((length, E))
    edges[E].append((length, D))

def dijkstra(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        now_dist, node = heappop(pq)
        if now_dist > dist[node]:
            continue

        for next_dist, next_node in edges[node]:
            new_dist = now_dist + next_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(pq, (new_dist, next_node))
    
    return dist

dist_A = dijkstra(A)
dist_B = dijkstra(B)
dist_C = dijkstra(C)

answer = -1
max_min_dist = -1

for i in range(1, N+1):
    min_dist = min(dist_A[i], dist_B[i], dist_C[i])
    if min_dist > max_min_dist:
        max_min_dist = min_dist
        answer = i

    elif min_dist == max_min_dist and i < answer:
        answer = i

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|203632|2280|PyPy3|1175
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

#### **📝해설**

```python
import sys
from heapq import heappush, heappop

INF = int(21e8)

# 입력받기
N = int(sys.stdin.readline().rstrip())
A, B, C = map(int, sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    D, E, length = map(int, sys.stdin.readline().rstrip().split())
    edges[D].append((length, E))
    edges[E].append((length, D))

# 시작지점을 입력받고, 다익스트라 알고리즘을 통해 각 노드까지의 최단거리를 리턴
def dijkstra(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        now_dist, node = heappop(pq)
        if now_dist > dist[node]:
            continue

        for next_dist, next_node in edges[node]:
            new_dist = now_dist + next_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(pq, (new_dist, next_node))
    
    return dist

# 각각 A, B, C에서 최단거리를 구함
dist_A = dijkstra(A)
dist_B = dijkstra(B)
dist_C = dijkstra(C)

# 가장 먼 노드
answer = -1

# 그 때의 거리
max_min_dist = -1

# 모든 노드를 확인하면서
for i in range(1, N+1):

    # 현재 노드에서 A, B, C까지의 최단 거리를 구함
    min_dist = min(dist_A[i], dist_B[i], dist_C[i])

    # 이 때 최단거리가 더 멀다면 갱신
    if min_dist > max_min_dist:
        max_min_dist = min_dist
        answer = i

    # 번호 갱신
    elif min_dist == max_min_dist and i < answer:
        answer = i

print(answer)
```