# [2098] 외판원 순회

### **난이도**
골드 1
## **📝문제**
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로 computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다. 여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다) 이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다. 모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다. 경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 16) 다음 N개의 줄에는 비용 행렬이 주어진다. 각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다. W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.
### **출력**
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
```

**예제 출력1**

```
35
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
INF = int(21e8)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(now, visited):
    if visited == (1 << N) - 1:
        return graph[now][0] if graph[now][0] > 0 else INF
    
    if dp[now][visited] != -1:
        return dp[now][visited]
    
    dp[now][visited] = INF
    
    for next in range(N):
        if visited & (1 << next) or graph[now][next] == 0:
            continue

        cost = graph[now][next] + tsp(next, visited | (1 << next))
        dp[now][visited] = min(dp[now][visited], cost)

    return dp[now][visited]

print(tsp(0, 1))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|119016|228|PyPy3|631
#### **📝해설**

**알고리즘**
```
1. 비트마스킹
2. DP
3. 외판원 순회 문제
```

### **다른 풀이**

```python
import sys

INF = 10**8
N = int(sys.stdin.readline().strip())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[INF] * (1 << N) for _ in range(N)]

for i in range(1, N):
    if W[0][i]:
        dp[i][1<<i | 1] = W[0][i]

for k in range(1 << N):
    for i in range(1,N):
        if dp[i][k] == INF:
            continue
        for j in range(1,N):
            if W[i][j] != 0 and k & (1<<j) == 0 and dp[j][k | 1<<j] > dp[i][k] + W[i][j]:
                dp[j][k | 1<<j] = dp[i][k] + W[i][j]

minimum = INF
for i in range(1,N):
    if W[i][0] != 0 and minimum > dp[i][(1<<N)-1] + W[i][0]:
        minimum = dp[i][(1<<N)-1] + W[i][0]
print(minimum)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
sssaic83|119016|180|PyPy3|673
#### **📝해설**

```python
INF = int(21e8)

# 입력받기
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# DP 배열 선언
# DP[i][visited], i : 현재 방문중인 노드, visited : 현재까지 방문한 노드를 비트로 표현
dp = [[-1] * (1 << N) for _ in range(N)]

# DFS로 방문
def tsp(now, visited):

    # 모든 노드를 방문했다면
    if visited == (1 << N) - 1:
        
        # 시작점으로 돌아가는 비용을 반환
        return graph[now][0] if graph[now][0] > 0 else INF
    
    # 이미 계산된 값이 있다면 그 값을 그대로 반환
    if dp[now][visited] != -1:
        return dp[now][visited]
    
    # DP 배열 방문 처리(초기화)
    dp[now][visited] = INF
    
    # 갈 수 있는 모든 노드를 검사하면서
    for next in range(N):

        # 이미 방문한 도시이거나, 길이 없는 경우 고려하지 않음
        if visited & (1 << next) or graph[now][next] == 0:
            continue
        
        # 새롭게 방문하는 비용을 계산
        cost = graph[now][next] + tsp(next, visited | (1 << next))

        # DP 배열을 초기화
        dp[now][visited] = min(dp[now][visited], cost)

    # 모든 노드를 순회하는 비용을 반환
    return dp[now][visited]

# 시작점을 0으로 두고 출발 (어느 노드에서 출발하더라도 순회하는 최소비용은 같다)
print(tsp(0, 1))
```