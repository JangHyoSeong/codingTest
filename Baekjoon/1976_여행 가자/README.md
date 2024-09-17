# [1976] 여행 가자

### **난이도**
골드 4
## **📝문제**
동혁이는 친구들과 함께 여행을 가려고 한다. 한국에는 도시가 N개 있고 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있다. 동혁이의 여행 일정이 주어졌을 때, 이 여행 경로가 가능한 것인지 알아보자. 물론 중간에 다른 도시를 경유해서 여행을 할 수도 있다. 예를 들어 도시가 5개 있고, A-B, B-C, A-D, B-D, E-A의 길이 있고, 동혁이의 여행 계획이 E C B C D 라면 E-A-B-C-B-C-B-D라는 여행경로를 통해 목적을 달성할 수 있다.

도시들의 개수와 도시들 간의 연결 여부가 주어져 있고, 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능한지 여부를 판별하는 프로그램을 작성하시오. 같은 도시를 여러 번 방문하는 것도 가능하다.
### **입력**
첫 줄에 도시의 수 N이 주어진다. N은 200이하이다. 둘째 줄에 여행 계획에 속한 도시들의 수 M이 주어진다. M은 1000이하이다. 다음 N개의 줄에는 N개의 정수가 주어진다. i번째 줄의 j번째 수는 i번 도시와 j번 도시의 연결 정보를 의미한다. 1이면 연결된 것이고 0이면 연결이 되지 않은 것이다. A와 B가 연결되었으면 B와 A도 연결되어 있다. 마지막 줄에는 여행 계획이 주어진다. 도시의 번호는 1부터 N까지 차례대로 매겨져 있다.
### **출력**
첫 줄에 가능하면 YES 불가능하면 NO를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
3
0 1 0
1 0 1
0 1 0
1 2 3
```

**예제 출력1**

```
YES
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
M = int(input())

edges = [[] for _ in range(N+1)]
for start_node in range(1, N+1):
    temp_edge = [0] + list(map(int, input().split()))
    for end_node in range(1, N+1):
        if temp_edge[end_node]:
            edges[start_node].append(end_node)
            edges[end_node].append(start_node)
    
travel = list(map(int, input().split()))

visited = [False] * (N+1)
q = deque()

q.append(travel[0])
visited[travel[0]] = True

while q:
    now_node = q.popleft()

    for next_node in edges[now_node]:
        if not visited[next_node]:
            q.append(next_node)
            visited[next_node] = True

for city in travel:
    if not visited[city]:
        print('NO')
        break
else:
    print('YES')
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34072|60|Python3|763
#### **📝해설**

**알고리즘**
```
1. BFS
2. Union-find
```

#### **😅개선점**

1. 다른 풀이로도 풀어보자
2. 
### **다른 풀이**

```python
[N], [M], *l = [map(int, e.split()) for e in open(0)]
p = [-1] * (N+1)

def find(x):
  if p[x] < 0:
    return x
  p[x] = find(p[x])
  return p[x]

def union(x, y):
  a = find(x)
  b = find(y)
  if a == b:
    return
  p[b] = a

for i in range(N):
  for j, k in enumerate(l[i]):
    if k == 1:
      union(i+1, j+1)

plan = list(l[-1])
ans = [e for e in plan if find(plan[0]) == find(e)]
print('YES') if len(ans) == M else print('NO')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rabi|31120|36|Python3|434
#### **📝해설**

```python
from collections import deque

N = int(input())
M = int(input())

# linkedlist의 형태로 간선 정보를 저장
edges = [[] for _ in range(N+1)]
for start_node in range(1, N+1):
    temp_edge = [0] + list(map(int, input().split()))
    for end_node in range(1, N+1):
        if temp_edge[end_node]:
            edges[start_node].append(end_node)
            edges[end_node].append(start_node)

travel = list(map(int, input().split()))

visited = [False] * (N+1)
q = deque()

# q 선언 및 초기 정보 삽입
q.append(travel[0])
visited[travel[0]] = True

# BFS 시작
while q:
    now_node = q.popleft()

    for next_node in edges[now_node]:
        if not visited[next_node]:
            q.append(next_node)
            visited[next_node] = True


# 만약 여행중에 방문하지 못한 도시가 있다면
for city in travel:

  # no를 출력하고 종료
    if not visited[city]:
        print('NO')
        break
# 모든 도시를 잘 방문했다면 YES
else:
    print('YES')
```