# [2458] 키 순서

### **난이도**
골드 4
## **📝문제**
1번부터 N번까지 번호가 붙여져 있는 학생들에 대하여 두 학생끼리 키를 비교한 결과의 일부가 주어져 있다. 단, N명의 학생들의 키는 모두 다르다고 가정한다. 예를 들어, 6명의 학생들에 대하여 6번만 키를 비교하였고, 그 결과가 다음과 같다고 하자.

- 1번 학생의 키 < 5번 학생의 키
- 3번 학생의 키 < 4번 학생의 키
- 5번 학생의 키 < 4번 학생의 키
- 4번 학생의 키 < 2번 학생의 키
- 4번 학생의 키 < 6번 학생의 키
- 5번 학생의 키 < 2번 학생의 키  
이 비교 결과로부터 모든 학생 중에서 키가 가장 작은 학생부터 자신이 몇 번째인지 알 수 있는 학생들도 있고 그렇지 못한 학생들도 있다는 사실을 아래처럼 그림을 그려 쉽게 확인할 수 있다. a번 학생의 키가 b번 학생의 키보다 작다면, a에서 b로 화살표를 그려서 표현하였다.

[이미지](https://upload.acmicpc.net/8f9e2484-a3aa-4b97-b1fa-387df4ae58d0/-/preview/)

1번은 5번보다 키가 작고, 5번은 4번보다 작기 때문에, 1번은 4번보다 작게 된다. 그러면 1번, 3번, 5번은 모두 4번보다 작게 된다. 또한 4번은 2번과 6번보다 작기 때문에, 4번 학생은 자기보다 작은 학생이 3명이 있고, 자기보다 큰 학생이 2명이 있게 되어 자신의 키가 몇 번째인지 정확히 알 수 있다. 그러나 4번을 제외한 학생들은 자신의 키가 몇 번째인지 알 수 없다.

학생들의 키를 비교한 결과가 주어질 때, 자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇 명인지 계산하여 출력하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 학생들의 수 N (2 ≤ N ≤ 500)과 두 학생 키를 비교한 횟수 M (0 ≤ M ≤ N(N-1)/2)이 주어진다.

다음 M개의 각 줄에는 두 학생의 키를 비교한 결과를 나타내는 N보다 작거나 같은 서로 다른 양의 정수 a와 b가 주어진다. 이는 번호가 a인 학생이 번호가 b인 학생보다 키가 작은 것을 의미한다.
### **출력**
자신이 키가 몇 번째인지 알 수 있는 학생이 모두 몇 명인지를 출력한다.
### **예제입출력**

**예제 입력1**

```
6 6
1 5
3 4
5 4
4 2
4 6
5 2
```

**예제 출력1**

```
1
```

**예제 입력2**

```
6 7
1 3
1 5
3 4
5 4
4 2
4 6
5 2
```

**예제 출력2**

```
2
```

**예제 입력3**

```
6 3
1 2
2 3
4 5
```

**예제 출력3**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[int(21e8)] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for edge in edges:
    graph[edge[0]][edge[1]] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

count = 0
for i in range(1, N+1):
    known_count = 0
    for j in range(1, N+1):
        if graph[i][j] == 1 or graph[j][i] == 1:
            known_count += 1
    
    if known_count == N-1:
        count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|123604|988|PyPy3|637
#### **📝해설**

**알고리즘**
```
1. 플로이드-워셜 알고리즘
```

### **다른 풀이**

```python
import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):
    visited= [False] * (N+1)
    cnt = 0
    q = deque()
    q.append(start)

    while(q):
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                Small[i] += 1
        cnt += 1

    return cnt-1 # cnt - 1은 내가 탐색한 노드의 수 즉, 나보다 키가 큰 사람들을 의미한다.

N,M = map(int,input().split())
graph = [[]for i in range(N+1)]
Tall = [0]*(N+1)
Small = [0] *(N+1)

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

for i in range(1,N+1):
    Tall[i] = BFS(i)

cnt = 0
for i in range(1,N+1):
    if Tall[i]+Small[i] == N-1:
        cnt +=1

print(cnt)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
wwqw58|118748|256|PyPy3|798
#### **📝해설**

```python
N, M = map(int, input().split())

# 플로이드-워셜 알고리즘을 위해 간선 정보를 하나의 리스트로 저장
edges = [list(map(int, input().split())) for _ in range(M)]

# 각 노드 사이의 이동 거리를 저장할 2차원 리스트
graph = [[int(21e8)] * (N+1) for _ in range(N+1)]

# 본인 노드로 이동하는 것은 거리가 0
for i in range(1, N+1):
    graph[i][i] = 0

# 모든 간선 정보를 입력
for edge in edges:
    graph[edge[0]][edge[1]] = 1

# 플로이드-워셜 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

# 키를 알 수 있는 사람의 수를 저장할 변수
count = 0

# 모든 사람들에 대해서 검사
for i in range(1, N+1):
    known_count = 0

    # 키의 대수관계를 알 수 있다면 카운트 ++
    for j in range(1, N+1):
        if graph[i][j] == 1 or graph[j][i] == 1:
            known_count += 1
    
    # 모든사람과의 키 관계가 정의되어 있다면 카운트 ++
    if known_count == N-1:
        count += 1

print(count)
```