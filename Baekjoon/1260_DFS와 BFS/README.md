# [1260] DFS와 BFS

### **난이도**
실버 2
## **📝문제**
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
### **입력**
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
### **출력**
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
### **예제입출력**

**예제 입력1**

```
4 5 1
1 2
1 3
1 4
2 4
3 4
```

**예제 출력1**

```
1 2 4 3
1 2 3 4
```

**예제 입력2**

```
5 5 3
5 4
5 2
1 2
3 4
3 1
```

**예제 출력2**

```
3 1 2 5 4
3 1 4 2 5
```

**예제 입력3**

```
1000 1 1000
999 1000
```

**예제 출력3**

```
1000 999
1000 999
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

def dfs(node, visited, result):
    visited[node] = True
    result.append(node)
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited, result)

def bfs(start):
    visited = [False] * (n + 1)
    result = []
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        result.append(node)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
    return result

visited_dfs = [False] * (n + 1)
dfs_result = []
dfs(v, visited_dfs, dfs_result)

bfs_result = bfs(v)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35448|68|Python3|1002
#### **📝해설**

**알고리즘**
```
1. DFS
2. BFS
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline


def dfs(v):
    vstd[v] = True
    smap[v].sort()
    result.append(v)
    for i in smap[v]:
        if not vstd[i]:
            dfs(i)

def bfs(v):
    queue = [v]
    vstd[v] = True
    result.append(v)
    while queue:
        d = queue.pop(0)
        for i in smap[d]:
            if not vstd[i]:
                queue.append(i)
                vstd[i] = True
                result.append(i)

N,M,V = map(int,input().split())
smap = [[] for i in range(N+1)]
vstd = [False] * (N+1)
result = []
for i in range(M):
    a,b = map(int, input().split())
    smap[a].append(b)
    smap[b].append(a)

dfs(V)
print(*result)
result = []
cnt = 1
vstd = [False] * (N+1)
bfs(V)
print(*result)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jbrandon413|32236|40|Python3|725
#### **📝해설**

```python
from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드 번호가 작은 순으로 방문할 수 있게 정렬
for g in graph:
    g.sort()

# 재귀함수를 통해 DFS
def dfs(node, visited, result):
    visited[node] = True
    result.append(node)
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited, result)

# BFS
def bfs(start):
    visited = [False] * (n + 1)
    result = []
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        result.append(node)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
    return result

visited_dfs = [False] * (n + 1)
dfs_result = []
dfs(v, visited_dfs, dfs_result)

bfs_result = bfs(v)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))
```