# [1516] 게임 개발

### **난이도**
골드 3
## **📝문제**
숌 회사에서 이번에 새로운 전략 시뮬레이션 게임 세준 크래프트를 개발하기로 하였다. 핵심적인 부분은 개발이 끝난 상태고, 종족별 균형과 전체 게임 시간 등을 조절하는 부분만 남아 있었다.

게임 플레이에 들어가는 시간은 상황에 따라 다를 수 있기 때문에, 모든 건물을 짓는데 걸리는 최소의 시간을 이용하여 근사하기로 하였다. 물론, 어떤 건물을 짓기 위해서 다른 건물을 먼저 지어야 할 수도 있기 때문에 문제가 단순하지만은 않을 수도 있다. 예를 들면 스타크래프트에서 벙커를 짓기 위해서는 배럭을 먼저 지어야 하기 때문에, 배럭을 먼저 지은 뒤 벙커를 지어야 한다. 여러 개의 건물을 동시에 지을 수 있다.

편의상 자원은 무한히 많이 가지고 있고, 건물을 짓는 명령을 내리기까지는 시간이 걸리지 않는다고 가정하자.
### **입력**
첫째 줄에 건물의 종류 수 N(1 ≤ N ≤ 500)이 주어진다. 다음 N개의 줄에는 각 건물을 짓는데 걸리는 시간과 그 건물을 짓기 위해 먼저 지어져야 하는 건물들의 번호가 주어진다. 건물의 번호는 1부터 N까지로 하고, 각 줄은 -1로 끝난다고 하자. 각 건물을 짓는데 걸리는 시간은 100,000보다 작거나 같은 자연수이다. 모든 건물을 짓는 것이 가능한 입력만 주어진다.
### **출력**
N개의 각 건물이 완성되기까지 걸리는 최소 시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
```

**예제 출력1**

```
10
20
14
18
17
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())

build_time = [0] * (N + 1)
total_time = [0] * (N + 1)
indegree = [0] * (N+1)
result = [0] * (N+1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N+1):
    time, *arr = list(map(int, input().split()))
    build_time[i] = time

    for prev in arr[:-1]:
        graph[prev].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        total_time[i] = build_time[i]

while q:
    now = q.popleft()

    for next in graph[now]:
        indegree[next] -= 1
        total_time[next] = max(total_time[next], total_time[now] + build_time[next])

        if indegree[next] == 0:
            q.append(next)

for i in range(1, N+1):
    print(total_time[i])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34976|96|Python3|767
#### **📝해설**

**알고리즘**
```
1. DP
2. 위상 정렬
```

### **다른 풀이**

```python
import sys

sys.setrecursionlimit(10 ** 9)

def dfs(idx):
    global dp
    if dp[idx] > 0:
        return dp[idx]
    if len(li[idx]) == 0:
        dp[idx] = time[idx]
        return time[idx]

    for i in li[idx]:
        val = time[idx] + dfs(i)
        if dp[idx] < val:
            dp[idx] = val
    return dp[idx]

N = int(sys.stdin.readline())
time = [0] * (N + 1)
li = [[] for _ in range(N + 1)]
dp = [0] * (N + 1)

for i in range(1, N + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    time[i] = temp[0]
    li[i] = temp[1:-1]

for i in range(1, N + 1):
    if dp[i] == 0:
        dfs(i)

for i in range(1, N + 1):
    print(dp[i])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jeong220722|32140|44|Python3|656
#### **📝해설**

```python
from collections import deque

N = int(input())

# 건물을 짓는 데 걸리는 시간
build_time = [0] * (N + 1)

# 앞선 건물을 다 짓고 건물을 짓는데 걸리는 시간
total_time = [0] * (N + 1)

# 선행되어야 하는 건물의 개수
indegree = [0] * (N+1)

# 선행되어야 하는 건물의 번호를 저장
graph = [[] for _ in range(N + 1)]

# 노드 추가
for i in range(1, N+1):
    time, *arr = list(map(int, input().split()))
    build_time[i] = time

    for prev in arr[:-1]:
        graph[prev].append(i)
        indegree[i] += 1

q = deque()

# 가장 먼저 지어도 되는 건물들을 먼저 확인
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        total_time[i] = build_time[i]

# BFS
while q:
    now = q.popleft()

    # 다음 건물들을 확인
    for next in graph[now]:

        # 차수를 낮추고
        indegree[next] -= 1

        # 기존에 걸리는 시간과, 현재 걸리는 시간 중 큰 값을 선택
        total_time[next] = max(total_time[next], total_time[now] + build_time[next])

        # 차수가 0이 된다면 큐에 삽입
        if indegree[next] == 0:
            q.append(next)

# 출력
for i in range(1, N+1):
    print(total_time[i])
```