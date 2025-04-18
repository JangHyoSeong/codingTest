# [6118] 숨바꼭질

### **난이도**
실버 1
## **📝문제**
재서기는 수혀니와 교외 농장에서 숨바꼭질을 하고 있다. 농장에는 헛간이 많이 널려있고 재서기는 그 중에 하나에 숨어야 한다. 헛간의 개수는 N(2 <= N <= 20,000)개이며, 1 부터 샌다고 하자.  

재서기는 수혀니가 1번 헛간부터 찾을 것을 알고 있다. 모든 헛간은 M(1<= M <= 50,000)개의 양방향 길로 이어져 있고, 그 양 끝을 A_i 와 B_i(1<= A_i <= N; 1 <= B_i <= N; A_i != B_i)로 나타낸다. 또한 어떤 헛간에서 다른 헛간으로는 언제나 도달 가능하다고 생각해도 좋다. 

재서기는 발냄새가 지독하기 때문에 최대한 냄새가 안나게 숨을 장소를 찾고자 한다. 냄새는 1번 헛간에서의 거리(여기서 거리라 함은 지나야 하는 길의 최소 개수이다)가 멀어질수록 감소한다고 한다. 재서기의 발냄새를 최대한 숨길 수 있는 헛간을 찾을 수 있게 도와주자!
### **입력**
첫 번째 줄에는 N과 M이 공백을 사이에 두고 주어진다.

이후 M줄에 걸쳐서 A_i와 B_i가 공백을 사이에 두고 주어진다.
### **출력**
출력은 한줄로 이루어지며, 세 개의 값을 공백으로 구분지어 출력해야한다. 

첫 번째는 숨어야 하는 헛간 번호를(만약 거리가 같은 헛간이 여러개면 가장 작은 헛간 번호를 출력한다), 두 번째는 그 헛간까지의 거리를, 세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력해야한다.
### **예제입출력**

**예제 입력1**

```
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
```

**예제 출력1**

```
4 2 3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [-1] * (N+1)
visited[1] = 0

q = deque([1])
while q:
    now = q.popleft()

    for next in edges[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1

max_dist = 0
max_dist_idx = 0
same_dist_count = 1
for i in range(1, N+1):
    if max_dist < visited[i]:
        max_dist = visited[i]
        max_dist_idx = i
        same_dist_count = 1
    
    elif max_dist == visited[i]:
        same_dist_count += 1

print(max_dist_idx, max_dist, same_dist_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|115596|180|PyPy3|776
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n_vertex, n_edges = map(int, input().split())
    graph = [[] for _ in range(n_vertex + 1)]
    count = dict()
    visited = [False] * (n_vertex + 1)
    for _ in range(n_edges):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited[1] = True
    q = deque()
    q.append((1, 0))
    while q:
        now, step = q.popleft()
        if step not in count:
            count[step] = []
        count[step].append(now)
        for nxt in graph[now]:
            if visited[nxt]:
                continue
            q.append((nxt, step + 1))
            visited[nxt] = True
    max_distance = max(count.keys())
    print(min(count[max_distance]), max_distance, len(count[max_distance]))


solution()

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
iamhelpingstar|39628|100|Python3|842
#### **📝해설**

```python
import sys
from collections import deque

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

# 방문 여부 저장 리스트. 값은 그 노드에 도달하기까지 거리
visited = [-1] * (N+1)
visited[1] = 0

# BFS를 위한 queue 선언
q = deque([1])
while q:
    now = q.popleft()

    # 다음 노드를 검사해서, 방문하지 않았다면 방문처리
    for next in edges[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1

# 최대로 떨어진 노드까지의 거리, 그때의 인덱스, 같은 거리의 노드들의 갯수
max_dist = 0
max_dist_idx = 0
same_dist_count = 1

# 노드들을 검사하면서 값들을 갱신
for i in range(1, N+1):
    if max_dist < visited[i]:
        max_dist = visited[i]
        max_dist_idx = i
        same_dist_count = 1
    
    elif max_dist == visited[i]:
        same_dist_count += 1

print(max_dist_idx, max_dist, same_dist_count)
```