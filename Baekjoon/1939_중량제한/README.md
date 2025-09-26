# [문제번호] 문제제목

### **난이도**
골드 3
## **📝문제**
N(2 ≤ N ≤ 10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다. 그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N, M(1 ≤ M ≤ 100,000)이 주어진다. 다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1 ≤ A, B ≤ N), C(1 ≤ C ≤ 1,000,000,000)가 주어진다. 이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다. 서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다. 마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다. 공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.
### **출력**
첫째 줄에 답을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
1 2 2
3 1 3
2 3 2
1 3
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

INF = float('inf')

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

start, end = map(int, sys.stdin.readline().rstrip().split())
weights = [0] * (N + 1)
weights[start] = INF

pq = [(-INF, start)]
while pq:
    
    now_weight, now_node = heappop(pq)
    now_weight *= -1

    if now_node == end:
        print(now_weight)
        break

    if now_weight < weights[now_node]:
        continue

    for next_weight, next_node in edges[now_node]:
        next_capacity = min(now_weight, next_weight)
        if next_capacity > weights[next_node]:
            weights[next_node] = next_capacity
            heappush(pq, (-next_capacity, next_node))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|124952|236|PyPy3|872
#### **📝해설**

**알고리즘**
```
1. DFS/BFS
2. 이분 탐색
3. 다익스트라
4. 분리집합
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def init():
    for _ in range(m):
        a, b, w = map(int, input().split())
        legs.append((w, a, b))
    legs.sort(reverse=True)

def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)

    if x < y: parent[y] = x
    else: parent[x] = y


n, m = map(int, input().split())
legs = []
init()

parent = [i for i in range(n+1)]
s, e = map(int, input().split())

for w, a, b in legs:
    union(a, b)

    if find(s) == find(e):
        print(w)
        break
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ever618|49576|184|Python3|603
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

INF = float('inf')

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

# 시작점, 끝점
start, end = map(int, sys.stdin.readline().rstrip().split())

# 해당 노드를 지날 때 가능한 최대 용량
weights = [0] * (N + 1)

# 시작점 초기화
weights[start] = INF

# 최대 힙을 사용
pq = [(-INF, start)]

while pq:
    
    now_weight, now_node = heappop(pq)
    now_weight *= -1

    # 도착지에 닿았다면 종료
    if now_node == end:
        print(now_weight)
        break
    
    # 최대용량보다 작은 상태라면 고려하지 않음
    if now_weight < weights[now_node]:
        continue

    # 다음 노드를 확인하면서
    for next_weight, next_node in edges[now_node]:

        # 가능한 최대 용량을 구함
        next_capacity = min(now_weight, next_weight)

        # 가능한 경우, 탐색
        if next_capacity > weights[next_node]:
            weights[next_node] = next_capacity
            heappush(pq, (-next_capacity, next_node))
```

### **🔖정리**

1. 간선을 정렬하고 분리집합 사용하는 방법이 있었다