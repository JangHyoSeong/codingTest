# [18232] 텔레포트 정거장

### **난이도**
실버 2
## **📝문제**
꽉꽉나라에 사는 주예와 방주는 점 S에서 만나 저녁을 먹기로 했다. 주예는 점 S에 도착했지만 길치인 방주가 약속시간이 30분이 지나도 나타나지 않자 방주에게 연락을 하여 방주가 점 E에 있다는 사실을 알아냈다. 주예는 방주에게 그 위치에 가만히 있으라고 했고, 직접 점 E로 가려고 한다.

꽉꽉나라에는 1부터 N까지의 각 점에 하나의 텔레포트 정거장이 위치해 있고 텔레포트를 통하여 연결되어 있는 다른 텔레포트의 정거장으로 이동할 수 있다. 주예는 현재 위치가 점 X라면 X+1이나 X-1로 이동하거나 X에 위치한 텔레포트와 연결된 지점으로 이동할 수 있으며 각 행동에는 1초가 소요된다. 배가 고픈 주예는 최대한 빨리 방주와 만나고 싶어 한다.

N과 텔레포트 연결 정보가 주어질 때 점 S에 있는 주예가 점 E까지 가는 최소 시간을 구해보자.
### **입력**
첫 번째 줄에 정수 N, M이 공백으로 구분되어 주어진다. (2 ≤ N ≤ 300,000, 0 ≤ M ≤ min(N×(N-1)/2, 300,000))

두 번째 줄에 정수 S, E가 공백으로 구분되어 주어진다. (1 ≤ S, E ≤ N, S ≠ E)

그 다음 줄부터 M개의 줄에 걸쳐 텔레포트 연결 정보를 의미하는 정수 x, y가 주어진다. (1 ≤ x, y ≤ N, x ≠ y)

x y는 점 x의 텔레포트와 점 y의 텔레포트가 연결되어 있다는 뜻이다. M개의 연결정보는 중복되는 x y쌍이 없도록 주어진다.
### **출력**
첫 번째 줄에 주예와 방주가 만날 수 있는 최소 시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 1
1 5
1 4
```

**예제 출력1**

```
2
```

**예제 입력2**

```
10 3
2 5
1 6
1 3
2 8
```

**예제 출력2**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
S, E = map(int, sys.stdin.readline().rstrip().split())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    edges[x].append(y)
    edges[y].append(x)

q = deque()
q.append(S)

visited = [-1] * (N+1)
visited[S] = 0

while q:
    now = q.popleft()

    for next in edges[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
            if next == E:
                print(visited[next])
                break
    
    for dx in [-1, 1]:
        next = now + dx

        if 1 <= next <= N and visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
            if next == E:
                print(visited[next])
                break
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|154500|628|PyPy3|884
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
S, E = map(int, sys.stdin.readline().rstrip().split())

# 간선 정보 입력
edges = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    edges[x].append(y)
    edges[y].append(x)

# BFS 사용을 위한 큐 선언
q = deque()
q.append(S)

# 방문 여부를 저장할 리스트. -1 : 방문하지 않은 노드, visited[i] : 노드에 방문하기 까지 걸린 시간
visited = [-1] * (N+1)
visited[S] = 0

# BFS 시작
while q:
    now = q.popleft()

    # 텔레포트 하는 경우
    for next in edges[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
            if next == E:
                print(visited[next])
                break
    
    # 1, -1로 움직이는 경우
    for dx in [-1, 1]:
        next = now + dx

        if 1 <= next <= N and visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
            if next == E:
                print(visited[next])
                break
```