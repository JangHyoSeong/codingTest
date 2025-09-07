# [16437] 양 구출 작전

### **난이도**
골드 3
## **📝문제**
N개의 섬으로 이루어진 나라가 있습니다. 섬들은 1번 섬부터 N번 섬까지 있습니다.

1번 섬에는 구명보트만 있고 다른 섬에는 양들 또는 늑대들이 살고 있습니다.

늘어나는 늑대의 개체 수를 감당할 수 없던 양들은 구명보트를 타고 늑대가 없는 나라로 이주하기로 했습니다.

각 섬에서 1번 섬으로 가는 경로는 유일하며 i번 섬에는 pi번 섬으로 가는 다리가 있습니다. 

양들은 1번 섬으로 가는 경로로 이동하며 늑대들은 원래 있는 섬에서 움직이지 않고 섬으로 들어온 양들을 잡아먹습니다. 늑대는 날렵하기 때문에 섬에 들어온 양을 항상 잡을 수 있습니다. 그리고 늑대 한 마리는 최대 한 마리의 양만 잡아먹습니다.

얼마나 많은 양이 1번 섬에 도달할 수 있을까요?
### **입력**
첫 번째 줄에 섬의 개수 N (2 ≤ N ≤ 123,456) 이 주어집니다.

두 번째 줄부터 N-1개에 줄에 2번 섬부터 N번 섬까지 섬의 정보를 나타내는 ti, ai, pi (1 ≤ ai ≤ 109, 1 ≤ pi ≤ N) 가 주어집니다.

ti가 'W' 인 경우 i번 섬에 늑대가 ai마리가 살고 있음을, ti가 'S'인 경우 i번 섬에 양이 ai마리가 살고 있음을 의미합니다. pi는 i번째 섬에서 pi번 섬으로 갈 수 있는 다리가 있음을 의미합니다.
### **출력**
첫 번째 줄에 구출할 수 있는 양의 수를 출력합니다.
### **예제입출력**

**예제 입력1**

```
4
S 100 3
W 50 1
S 10 1
```

**예제 출력1**

```
60
```

**예제 입력2**

```
7
S 100 1
S 100 1
W 100 1
S 1000 2
W 1000 2
S 900 6
```

**예제 출력2**

```
1200
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.setrecursionlimit(123456)

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
nodes = [('', 0)] * (N + 1)

for i in range(2, N+1):
    t, a, p = sys.stdin.readline().rstrip().split()
    a, p = int(a), int(p)
    graph[p].append(i)
    nodes[i] = (t, a)

def dfs(node):
    total_sheep = 0
    for child in graph[node]:
        total_sheep += dfs(child)

    t, a = nodes[node]
    if t == 'W':
        if total_sheep > a:
            return total_sheep - a
        
        else:
            return 0
    
    elif t == 'S':
        return total_sheep + a
    else:
        return total_sheep

print(dfs(1))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|412940|488|PyPy3|644
#### **📝해설**

**알고리즘**
```
1. DFS
2. 트리
```

### **다른 풀이**

```python
import sys

n = int(sys.stdin.readline())
indegree = [0] * (n + 1)
par = [0] * (n + 1)
sheep = [0] * (n + 1)

for i in range(1, n):
    t, cnt, nxt = sys.stdin.readline().split()
    cnt = int(cnt)
    nxt = int(nxt)

    if t == 'W':
        cnt *= -1
    
    indegree[nxt] += 1
    sheep[i + 1] = cnt
    par[i + 1] = nxt

que = []
front = 0 
rear = 0

for i in range(n):
    if indegree[i + 1] == 0:
        que.append(i + 1)
        rear += 1

while front < rear:
    cur = que[front]
    nxt = par[cur]
    cnt = sheep[cur]

    front += 1

    sheep[nxt] += max(cnt, 0)
    indegree[nxt] -= 1

    if indegree[nxt] == 0:
        que.append(nxt)
        rear += 1

print(max(sheep[1], 0))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
juchan1220|126312|224|PyPy3|694
#### **📝해설**

```python
import sys
sys.setrecursionlimit(123456)

N = int(sys.stdin.readline().rstrip())

# 자식 노드의 정보를 저장
graph = [[] for _ in range(N+1)]

# 각 노드에 양, 혹은 늑대가 몇마리인지 저장
nodes = [('', 0)] * (N + 1)

# 입력받기
for i in range(2, N+1):
    t, a, p = sys.stdin.readline().rstrip().split()
    a, p = int(a), int(p)
    graph[p].append(i)
    nodes[i] = (t, a)

# DFS를 통해 루트노드까지 탐색 후 값을 확인
def dfs(node):
    total_sheep = 0

    # 일단 자식 노드로 계속 깊게 들어가며 탐색
    for child in graph[node]:
        total_sheep += dfs(child)

    # 리프노드까지 왔다면 양, 늑대 개수를 더함
    t, a = nodes[node]

    # 늑대인 경우
    if t == 'W':

        # 양이 늑대보다 많다면 값을 줄임
        if total_sheep > a:
            return total_sheep - a
        
        # 늑대가 양보다 많다면 0
        else:
            return 0
    
    # 양인 경우
    elif t == 'S':

        # 양의 개수를 더함
        return total_sheep + a
    
    # 루트노드인 경우 최종적으로 리턴
    else:
        return total_sheep

# 루트노드부터 시작
print(dfs(1))
```