# [1167] 트리의 지름

### **난이도**
골드 2
## **📝문제**
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.
### **입력**
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.
### **출력**
첫째 줄에 트리의 지름을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
```

**예제 출력1**

```
11
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

V = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    node = data[0]
    idx = 1
    while data[idx] != -1:
        neighbor = data[idx]
        weight = data[idx + 1]
        graph[node].append((neighbor, weight))
        graph[neighbor].append((node, weight))

        idx += 2

def dfs(start):
    visited = [False] * (V + 1)
    distance = [0] * (V + 1)
    stack = [(start, 0)]

    while stack:
        node, dist = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        distance[node] = dist
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                stack.append((neighbor, dist + weight))
    return distance

dist = dfs(1)
farthest_node = dist.index(max(dist))

far_dist = dfs(farthest_node)
print(max(far_dist))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|170112|368|PyPy3|922
#### **📝해설**

**알고리즘**
```
1. 트리
2. DFS
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
INF = float("inf")

v = int(input().rstrip())
tree = [ [] for _ in range(v+1) ]
dist = [INF]*(v+1)

for _ in range(1, v+1):
	tmp = list(map(int,input().split()))
	for j in range(1, len(tmp)-1, 2):
		tree[tmp[0]].append((tmp[j], tmp[j+1]))

def dfs_stack(start): 
	global dist
	dist = [INF]*(v+1)
	dist[start] = 0
	stack = [start]
	while stack:
		now = stack.pop()
		for nxt in tree[now]:
			if dist[nxt[0]] == INF:  # 가 본 적이 없다면
				dist[nxt[0]] = dist[now]+nxt[1] # min 안 해도 된다
				stack.append(nxt[0])
	
dfs_stack(1)
dist[0] = 0
dfs_stack(dist.index(max(dist)))
dist[0] = 0
print(max(dist))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
koios|148184|236|PyPy3|654
#### **📝해설**

```python
import sys

# 입력받기
V = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    # 간선 정보를 저장
    node = data[0]
    idx = 1
    while data[idx] != -1:
        neighbor = data[idx]
        weight = data[idx + 1]
        graph[node].append((neighbor, weight))
        graph[neighbor].append((node, weight))

        idx += 2

# DFS 함수. 시작점을 매개변수로 입력받음
def dfs(start):

    # 노드의 방문 여부를 저장할 리스트
    visited = [False] * (V + 1)

    # 각 노드까지의 거리를 저장할 리스트
    distance = [0] * (V + 1)

    # 시작점 초기화
    stack = [(start, 0)]

    # DFS 시작
    while stack:
        node, dist = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        distance[node] = dist
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                stack.append((neighbor, dist + weight))
    return distance

# 임의의 한 점에서 DFS를 시작
dist = dfs(1)

# 이 점에서 가장 멀리 떨어진 노드는 트리 지름의 양 끝점중 하나
farthest_node = dist.index(max(dist))

# 이 점에서부터 다시 DFS
far_dist = dfs(farthest_node)

# 트리의 지름 출력
print(max(far_dist))
```