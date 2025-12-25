# [1240] 노드사이의 거리

### **난이도**
골드 5
## **📝문제**
$N$개의 노드로 이루어진 트리가 주어지고 M개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.
### **입력**
첫째 줄에 노드의 개수 
$N$과 거리를 알고 싶은 노드 쌍의 개수 
$M$이 입력되고 다음 
$N-1$개의 줄에 트리 상에 연결된 두 점과 거리를 입력받는다. 그 다음 줄에는 거리를 알고 싶은 
$M$개의 노드 쌍이 한 줄에 한 쌍씩 입력된다.
### **출력**
 
$M$개의 줄에 차례대로 입력받은 두 노드 사이의 거리를 출력한다.
### **예제입출력**

**예제 입력1**

```
4 2
2 1 2
4 3 2
1 4 3
1 2
3 2
```

**예제 출력1**

```
2
7
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    visited = [-1] * (N+1)
    visited[a] = 0

    q = deque()
    q.append(a)

    while q:
        now = q.popleft()

        for next_dist, next_node in edges[now]:
            if visited[next_node] == -1:
                visited[next_node] = visited[now] + next_dist
                if next_node == b:
                    q = deque()
                    break
                q.append(next_node)
    
    print(visited[b])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34944|308|Python3|775
#### **📝해설**

**알고리즘**
```
1. 트리
2. BFS
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def dfs(root):
    parents = [-1]*(N+1)
    parents[root] = root
    stack = [(root, 0)]

    while stack:
        cur, depth = stack.pop()

        for node, _ in edges[cur]:
            if parents[node] == -1:
                parents[node] = cur
                level[node] = depth+1
                stack.append((node, depth+1))
    return parents

def NCA(a, b):
    result = 0

    while level[a] != level[b]:
        if level[a] > level[b]:
            pa = parents[a]
            result += distances[a, pa]
            a = pa
        else:
            pb = parents[b]
            result += distances[b, pb]
            b = pb

    while a!=b:
        pa = parents[a]
        pb = parents[b]

        result += distances[a, pa] + distances[b, pb]
        a, b = pa, pb
        
    return result

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
distances = {}
level = [0]*(N+1)

for _ in range(N-1):
    u, v, w = map(int, input().split())

    distances[u, v] = w
    distances[v, u] = w

    edges[u].append([v, w])
    edges[v].append([u, w])

root = 1
parents = dfs(root)

for _ in range(M):
    a, b = map(int, input().split())
    result = NCA(a, b)
    print(result)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
qwqw8019|31120|36|Python3
#### **📝해설**

```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

# 입력받기
for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

# 거리 측정
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    visited = [-1] * (N+1)
    visited[a] = 0

    q = deque()
    q.append(a)

    while q:
        now = q.popleft()

        for next_dist, next_node in edges[now]:
            if visited[next_node] == -1:
                visited[next_node] = visited[now] + next_dist
                if next_node == b:
                    q = deque()
                    break
                q.append(next_node)
    
    print(visited[b])
```