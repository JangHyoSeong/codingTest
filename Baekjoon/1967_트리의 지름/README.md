# [1967] 트리의 지름

### **난이도**
골드 4
## **📝문제**
트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.

[이미지](https://www.acmicpc.net/JudgeOnline/upload/201007/ttrrtrtr.png)

이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.

[이미지](https://www.acmicpc.net/JudgeOnline/upload/201007/tttttt.png)

트리의 노드는 1부터 n까지 번호가 매겨져 있다.
### **입력**
파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.
### **출력**
첫째 줄에 트리의 지름을 출력한다.
### **예제입출력**

**예제 입력1**

```
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
```

**예제 출력1**

```
45
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

max_dist = 0
for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True

    stack = [(i, 0)]
    while stack:
        now, dist = stack.pop()
        max_dist = max(max_dist, dist)
        for next_dist, next_node in edges[now]:
            if visited[next_node]:
                continue

            stack.append((next_node, next_dist + dist))
            visited[next_node] = True

print(max_dist)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|210908|5316|PyPy3|643
#### **📝해설**

**알고리즘**
```
1. DFS
```

#### **😅개선점**

1. 더 효율적인 코드가 있을듯?

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(20_000)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))

maxlen = [0 for _ in range(n+1)]
def dfs(n):
    if len(graph[n]) == 0:
        return 0
    elif len(graph[n]) == 1:
        c, w = graph[n][0]
        maxlen[n] = dfs(c) + w
        return maxlen[n]
    else:
        cs = sorted([dfs(c)+w for c, w in graph[n]], reverse=True)
        maxlen[n] = cs[0] + cs[1]
        return cs[0]

dfs(1)
print(max(maxlen))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
good1588|34572|48|Python3|568
#### **📝해설**

```python
import sys

# 입력받기
N = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(N+1)]

# 간선 정보 저장
for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

# 최대 가중치
max_dist = 0

# 모든 노드에서 시작점을 잡음
for i in range(1, N+1):

    # 방문 여부 저장
    visited = [False] * (N+1)
    visited[i] = True

    # DFS를 위한 스택
    stack = [(i, 0)]

    # DFS
    while stack:
        now, dist = stack.pop()

        # 방문지점마다 최대 거리를 갱신
        max_dist = max(max_dist, dist)
        for next_dist, next_node in edges[now]:
            if visited[next_node]:
                continue

            stack.append((next_node, next_dist + dist))
            visited[next_node] = True

print(max_dist)
```