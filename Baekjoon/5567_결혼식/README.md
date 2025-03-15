# [5567] 결혼식

### **난이도**
실버 2
## **📝문제**
상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다. 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.

상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 상근이의 동기의 수 n (2 ≤ n ≤ 500)이 주어진다. 둘째 줄에는 리스트의 길이 m (1 ≤ m ≤ 10000)이 주어진다. 다음 줄부터 m개 줄에는 친구 관계 ai bi가 주어진다. (1 ≤ ai < bi ≤ n) ai와 bi가 친구라는 뜻이며, bi와 ai도 친구관계이다. 
### **출력**
첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
6
5
1 2
1 3
3 4
2 3
4 5
```

**예제 출력1**

```
3
```

**예제 입력2**

```
6
5
2 3
3 4
4 5
5 6
2 5
```

**예제 출력2**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
M = int(input())

parent = list(range(N+1))

edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (N+1)

visited[1] = True
q = deque([(1, 0)])
count = 0

while q:
    now, depth = q.popleft()

    for next in edges[now]:
        if visited[next]:
            continue
        
        if depth < 2:
            q.append((next, depth+1))
            visited[next] = True
            count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34924|320|Python3|558
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

# 입력받기
N = int(input())
M = int(input())

# 간선정보
edges = [[] for _ in range(N+1)]

# 간선 입력
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# 방문여부
visited = [False] * (N+1)

# 초기 정보
visited[1] = True

# 현재 친구 번호, 친구 관계의 깊이
q = deque([(1, 0)])
count = 0

# BFS
while q:
    now, depth = q.popleft()

    # 친구들을 검사하면서
    for next in edges[now]:

        # 이미 추가된 친구라면 고려하지 않음
        if visited[next]:
            continue
        
        # 친구의 친구까지만 검사
        if depth < 2:
            q.append((next, depth+1))
            visited[next] = True
            count += 1

print(count)
```