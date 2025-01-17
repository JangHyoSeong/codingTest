# [11779] 최소비용 구하기 2

### **난이도**
골드 3
## **📝문제**
n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 항상 시작점에서 도착점으로의 경로가 존재한다.
### **입력**
첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.
### **출력**
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.

셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다. 경로가 여러가지인 경우 아무거나 하나 출력한다.
### **예제입출력**

**예제 입력1**

```
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
```

**예제 출력1**

```
4
3
1 3 5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    edges[u].append((w, v))

start, end = map(int, sys.stdin.readline().rstrip().split())

INF = int(21e8)
dist = [INF] * (N+1)
parent = [-1] * (N+1)

pq = []
heappush(pq, (0, start))
dist[start] = 0

while pq:
    now_dist, now_node = heappop(pq)

    if dist[now_node] < now_dist:
        continue

    for next_dist, next_node in edges[now_node]:
        
        new_dist = next_dist + dist[now_node]
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            parent[next_node] = now_node
            heappush(pq, (new_dist, next_node))

print(dist[end])

path = []
node = end
while node != -1:
    path.append(node)
    node = parent[node]

path.reverse()
print(len(path))
print(" ".join(map(str, path)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|121400|240|PyPy3|981
#### **📝해설**

**알고리즘**
```
1. 다익스트라
```

#### **📝해설**

```python
import sys
from heapq import heappop, heappush

# 입력받기
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())

    # 다익스트라를 위해 비용을 앞에 저장
    edges[u].append((w, v))

start, end = map(int, sys.stdin.readline().rstrip().split())

INF = int(21e8)
dist = [INF] * (N+1)

# 어느 노드에서 왔는지 정보를 저장할 리스트
parent = [-1] * (N+1)

pq = []
heappush(pq, (0, start))
dist[start] = 0

# 다익스트라
while pq:
    now_dist, now_node = heappop(pq)

    if dist[now_node] < now_dist:
        continue

    for next_dist, next_node in edges[now_node]:
        
        new_dist = next_dist + dist[now_node]
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            # 어느 노드에서 이동해왔는지 정보를 저장
            parent[next_node] = now_node
            heappush(pq, (new_dist, next_node))

print(dist[end])

# 경로 출력
path = []
node = end
while node != -1:
    path.append(node)
    node = parent[node]

path.reverse()
print(len(path))
print(" ".join(map(str, path)))
```

### **🔖정리**

1. 다익스트라에서 경로를 출력하는 방법을 배웠다