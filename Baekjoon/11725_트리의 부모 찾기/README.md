# [11725] 트리의 부모 찾기

### **난이도**
실버 2
## **📝문제**
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
### **출력**
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
### **예제입출력**

**예제 입력1**

```
7
1 6
6 3
3 5
4 1
2 4
4 7
```

**예제 출력1**

```
4
6
1
3
1
4
```

**예제 입력2**

```
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
```

**예제 출력2**

```
1
1
2
3
3
4
4
5
5
6
6
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())

visited = [False] * (N+1)
edge = [[] for _ in range(N+1)]
parent = [None] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

q = deque()
q.append(1)
visited[1] = True

while q:

    node = q.popleft()

    for i in edge[node]:
        if not visited[i]:
            parent[i] = node
            visited[i] = True
            q.append(i)
    
    
for i in range(2, N+1):
    print(parent[i])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|129040|316|PyPy3|501
#### **📝해설**

**알고리즘**
```
1. DFS
2. 트리
```

### **다른 풀이**

```python
import sys; input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1]

while stack:
    node = stack.pop()
    for i in graph[node]:
        if parent[i] == 0:
            parent[i] = node
            stack.append(i)

print('\n'.join(map(str,parent[2:])))
```