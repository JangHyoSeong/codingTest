# [1613] 역사

### **난이도**
골드 3
## **📝문제**
역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다. 즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.

세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 주어진 사건들의 전후 관계도 알 수 있을까? 이를 해결하는 프로그램을 작성해 보도록 하자.
### **입력**
첫째 줄에 첫 줄에 사건의 개수 n(400 이하의 자연수)과 알고 있는 사건의 전후 관계의 개수 k(50,000 이하의 자연수)가 주어진다. 다음 k줄에는 전후 관계를 알고 있는 두 사건의 번호가 주어진다. 이는 앞에 있는 번호의 사건이 뒤에 있는 번호의 사건보다 먼저 일어났음을 의미한다. 물론 사건의 전후 관계가 모순인 경우는 없다. 다음에는 사건의 전후 관계를 알고 싶은 사건 쌍의 수 s(50,000 이하의 자연수)이 주어진다. 다음 s줄에는 각각 서로 다른 두 사건의 번호가 주어진다. 사건의 번호는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.
### **출력**
s줄에 걸쳐 물음에 답한다. 각 줄에 만일 앞에 있는 번호의 사건이 먼저 일어났으면 -1, 뒤에 있는 번호의 사건이 먼저 일어났으면 1, 어떤지 모르면(유추할 수 없으면) 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 5
1 2
1 3
2 3
3 4
2 4
3
1 5
2 4
3 1
```

**예제 출력1**

```
0
-1
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, K = map(int, input().split())

dist = [[0] * (N+1) for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    dist[a][b] = -1
    dist[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N + 1):
            if dist[i][k] == -1 and dist[k][j] == -1:
                dist[i][j] = -1
                dist[j][i] = 1

S = int(input())
for _ in range(S):
    x, y = map(int, input().split())
    print(dist[x][y])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|113352|2104|PyPy3|470
#### **📝해설**

**알고리즘**
```
1. 플로이드 워셜
2. 위상 정렬
```
### **다른 풀이**

```python
from sys import stdin, stdout
from collections import deque
n, k = map(int, stdin.readline().split())
ind = [0]*(n + 1)
graph = [[] for _ in range(n + 1)]
history = [0]*(n + 1)
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    ind[b] += 1
q = deque(i for i, v in enumerate(ind) if i and not v)
while q:
    cur = q.popleft()
    for nex in graph[cur]:
        history[nex] |= 1 << cur
        history[nex] |= history[cur]
        ind[nex] -= 1
        if not ind[nex]:
            q.append(nex)
stdin.readline()
ans = []
for a, b in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    if history[a] & (1 << b):
        ans.append(1)
    elif history[b] & (1 << a):
        ans.append(-1)
    else:
        ans.append(0)
stdout.write("\n".join(map(str, ans)))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
line1029|36508|184|Python3|815
#### **📝해설**

```python
N, K = map(int, input().split())

# 사건 관계를 저장할 2차원 리스트
dist = [[0] * (N+1) for _ in range(N+1)]

# 입력받으면서 초기 정보 기입
for _ in range(K):
    a, b = map(int, input().split())
    dist[a][b] = -1
    dist[b][a] = 1

# 플로이드-워셜 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N + 1):
            if dist[i][k] == -1 and dist[k][j] == -1:
                dist[i][j] = -1
                dist[j][i] = 1

# 출력
S = int(input())
for _ in range(S):
    x, y = map(int, input().split())
    print(dist[x][y])
```