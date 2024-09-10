# [18352] 특정 거리의 도시 찾기

### **난이도**
실버 2
## **📝문제**
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.  2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.
### **입력**
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.
### **출력**
X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 4 2 1
1 2
1 3
2 3
2 4
```

**예제 출력1**

```
4
```

**예제 입력2**

```
4 3 2 1
1 2
1 3
1 4
```

**예제 출력2**

```
-1
```

**예제 입력3**

```
4 4 1 1
1 2
1 3
2 3
2 4
```

**예제 출력3**

```
2
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M, K, X = map(int, input().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)

min_range = [float('inf')] * (N+1)
min_range[X] = 0

q = deque()
q.append([X, 0])

result = []

while q:
    now_node, count = q.popleft()

    for next_node in edge[now_node]:

        if count+1 < min_range[next_node]:
            min_range[next_node] = count+1
            if count+1 == K:
                result.append(next_node)
            elif count+1 < K:
                q.append([next_node, count+1])

result.sort()
if result:
    for node in result:
        print(node)
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|156948|880|PyPy3|681
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
edge_list = []
distance = [sys.maxsize] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    edge_list.append((A, B))

distance[X] = 0
for _ in range(K):
    for a, b in edge_list:
        if distance[a] != sys.maxsize and distance[b] > distance[a] + 1:
            distance[b] = distance[a] + 1

if distance.count(K) == 0:
    print(-1)
    exit()

for i in range(1, N + 1):
    if distance[i] == K:
        print(i)

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hwakyung99|205056|556|PyPy3|514
#### **📝해설**

```python
from collections import deque

N, M, K, X = map(int, input().split())

# 간선 정보를 저장
edge = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)

# 각 노드까지의 최단거리를 저장할 리스트
min_range = [float('inf')] * (N+1)

# 시작 노드 초기화
min_range[X] = 0


# BFS를 위한 q 선언
q = deque()
q.append([X, 0])

result = []

while q:
    now_node, count = q.popleft()

    # 갈 수 있는 노드를 모두 탐색
    for next_node in edge[now_node]:

        # 만약 이번 이동이 최단거리라면
        if count+1 < min_range[next_node]:

            # 최단거리를 갱신
            min_range[next_node] = count+1

            # K번의 이동이었다면 결과에 삽입
            if count+1 == K:
                result.append(next_node)

            # 아직 K번에 도달하지 않았다면 큐에 삽입
            elif count+1 < K:
                q.append([next_node, count+1])

result.sort()
if result:
    for node in result:
        print(node)
else:
    print(-1)
```