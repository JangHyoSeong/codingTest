# [14284] 간선 이어가기 2

### **난이도**
골드 5
## **📝문제**
정점 n개, 0개의 간선으로 이루어진 무방향 그래프가 주어진다. 그리고 m개의 가중치 간선의 정보가 있는 간선리스트가 주어진다. 간선리스트에 있는 간선 하나씩 그래프에 추가해 나갈 것이다. 이때, 특정 정점 s와 t가 연결이 되는 시점에서 간선 추가를 멈출 것이다. 연결이란 두 정점이 간선을 통해 방문 가능한 것을 말한다.

s와 t가 연결이 되는 시점의 간선의 가중치의 합이 최소가 되게 추가하는 간선의 순서를 조정할 때, 그 최솟값을 구하시오.
### **입력**
첫째 줄에 정점의 개수 n, 간선리스트의 간선 수 m이 주어진다.(2≤n≤5000,1≤m≤100,000)

다음 m줄에는 a,b,c가 주어지는데, 이는 a와 b는 c의 가중치를 가짐을 말한다. (1≤a,b≤n,1≤c≤100,a≠b)

다음 줄에는 두 정점 s,t가 주어진다. (1≤s,t≤n,s≠t)

모든 간선을 연결하면 그래프는 연결 그래프가 됨이 보장된다.
### **출력**
s와 t가 연결되는 시점의 간선의 가중치 합의 최솟값을 출력하시오,
### **예제입출력**

**예제 입력1**

```
8 9
1 2 3
1 3 2
1 4 4
2 5 2
3 6 1
4 7 3
5 8 6
6 8 2
7 8 7
1 8
```

**예제 출력1**

```
5
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
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

s, t = map(int, sys.stdin.readline().rstrip().split())
dist = [float('inf')] * (N+1)
dist[s] = 0

pq = [(0, s)]
while pq:
    now_dist, now_node = heappop(pq)

    if now_dist > dist[now_node]:
        continue

    for next_dist, next_node in edges[now_node]:
        new_dist = now_dist + next_dist
        if dist[next_node] > new_dist:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    
print(dist[t])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|121436|232|PyPy3|720
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

### **다른 풀이**

```python
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
routes = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, v = map(int, sys.stdin.readline().split())
    routes[s].append((e, v))
    routes[e].append((s, v))

ss, ee = map(int, sys.stdin.readline().split())

visit = [False] * (n+1)
hq = []

for e, c in routes[ss]:
    heapq.heappush(hq, (c, e))

while hq:
    c, v = heapq.heappop(hq)
    if visit[v]: continue
    visit[v] = True

    if v == ee:
        print(c)
        break

    for e, cc in routes[v]:
        heapq.heappush(hq, (cc + c, e))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20230660|55988|196|Python3|575