# [6497] 전력난

### **난이도**
골드 4
## **📝문제**
성진이는 한 도시의 시장인데 거지라서 전력난에 끙끙댄다. 그래서 모든 길마다 원래 켜져 있던 가로등 중 일부를 소등하기로 하였다. 길의 가로등을 켜 두면 하루에 길의 미터 수만큼 돈이 들어가는데, 일부를 소등하여 그만큼의 돈을 절약할 수 있다.

그러나 만약 어떤 두 집을 왕래할 때, 불이 켜져 있지 않은 길을 반드시 지나야 한다면 위험하다. 그래서 도시에 있는 모든 두 집 쌍에 대해, 불이 켜진 길만으로 서로를 왕래할 수 있어야 한다.

위 조건을 지키면서 절약할 수 있는 최대 액수를 구하시오.
### **입력**
입력은 여러 개의 테스트 케이스로 구분되어 있다.

각 테스트 케이스의 첫째 줄에는 집의 수 m과 길의 수 n이 주어진다. (1 ≤ m ≤ 200000, m-1 ≤ n ≤ 200000)

이어서 n개의 줄에 각 길에 대한 정보 x, y, z가 주어지는데, 이는 x번 집과 y번 집 사이에 양방향 도로가 있으며 그 거리가 z미터라는 뜻이다. (0 ≤ x, y < m, x ≠ y)

도시는 항상 연결 그래프의 형태이고(즉, 어떤 두 집을 골라도 서로 왕래할 수 있는 경로가 있다), 도시상의 모든 길의 거리 합은 231미터보다 작다.

입력의 끝에서는 첫 줄에 0이 2개 주어진다.
### **출력**
각 테스트 케이스마다 한 줄에 걸쳐 절약할 수 있는 최대 비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
0 0
```

**예제 출력1**

```
51
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappop, heappush

while True:
    M, N = map(int, sys.stdin.readline().rstrip().split())
    if M == 0 and N == 0:
        break

    edges = [[] for _ in range(M)]
    total_weight = 0

    for _ in range(N):
        x, y, z = map(int, sys.stdin.readline().rstrip().split())
        edges[x].append((z, y))
        edges[y].append((z, x))
        total_weight += z

    visited = [False] * M
    pq = [(0, 0)]
    min_weight = 0

    while pq:
        weight, u = heappop(pq)

        if visited[u]:
            continue
        visited[u] = True
        min_weight += weight

        for w, v in edges[u]:
            if not visited[v]:
                heappush(pq, (w, v))

    print(total_weight - min_weight)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|222480|1452|PyPy3|794
#### **📝해설**

**알고리즘**
```
1. 최소 스패닝 트리
```

### **다른 풀이**

```python
import sys
input=sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        parent[a]=parent[b]
    else:
        parent[b]=parent[a]

while 1:
    m,n=map(int,input().split())
    if m+n==0:
        break
    graph=[]
    for i in range(n):
        a,b,c=map(int,input().split())
        graph.append((c,a,b))
    graph.sort(key=lambda x:x[0])

    parent=list(range(m))

    ans=0
    for i in graph:
        if find(i[1])==find(i[2]):
            ans+=i[0]
            continue
        union(i[1],i[2])
    print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tobey2j0|215380|564|PyPy3|636
#### **📝해설**

```python
import sys
from heapq import heappop, heappush

# Prim 알고리즘
while True:
    M, N = map(int, sys.stdin.readline().rstrip().split())
    if M == 0 and N == 0:
        break
    
    # 간선 정보 저장
    edges = [[] for _ in range(M)]

    # 간선의 총 가중치
    total_weight = 0

    for _ in range(N):
        x, y, z = map(int, sys.stdin.readline().rstrip().split())
        edges[x].append((z, y))
        edges[y].append((z, x))
        total_weight += z

    # 각 정점의 방문 여부 검사
    visited = [False] * M

    # 0인 정점부터 각 노드까지의 최단거리를 방문하기 위한 우선순위 큐
    pq = [(0, 0)]

    # 필요한 간선만 유지했을 때의 가중치
    min_weight = 0

    # 탐색 시작
    while pq:

        # 현재 가중치, 간선
        weight, u = heappop(pq)

        # 이미 방문한 노드의 경우 고려하지 않음
        if visited[u]:
            continue

        # 방문 처리
        visited[u] = True

        # 최소 가중치에 더함
        min_weight += weight

        # 현재 노드에서 갈 수 있는 노드를 전부 탐색하면서
        for w, v in edges[u]:

            # 방문하지 않은 노드의 경우 우선순위 큐에 삽입
            if not visited[v]:
                heappush(pq, (w, v))

    # 정답 출력
    print(total_weight - min_weight)
```