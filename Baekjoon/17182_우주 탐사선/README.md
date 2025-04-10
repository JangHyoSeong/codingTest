# [17182] 우주 탐사선

### **난이도**
골드 3
## **📝문제**
우주 탐사선 ana호는 어떤 행성계를 탐사하기 위해 발사된다. 모든 행성을 탐사하는데 걸리는 최소 시간을 계산하려 한다. 입력으로는 ana호가 탐색할 행성의 개수와 ana호가 발사되는 행성의 위치와 ana호가 행성 간 이동을 하는데 걸리는 시간이 2차원 행렬로 주어진다. 행성의 위치는 0부터 시작하여 0은 행렬에서 0번째 인덱스에 해당하는 행성을 의미한다. 2차원 행렬에서 i, j 번 요소는 i 번째 행성에서 j 번째 행성에 도달하는데 걸리는 시간을 나타낸다. i와 j가 같을 때는 항상 0이 주어진다. 모든 행성을 탐사하는데 걸리는 최소 시간을 계산하여라.

탐사 후 다시 시작 행성으로 돌아올 필요는 없으며 이미 방문한 행성도 중복해서 갈 수 있다.
### **입력**
첫 번째 줄에는 행성의 개수 N과 ana호가 발사되는 행성의 위치 K가 주어진다. (2 ≤ N ≤ 10, 0 ≤ K < N)

다음 N 줄에 걸쳐 각 행성 간 이동 시간 Tij 가 N 개 씩 띄어쓰기로 구분되어 주어진다. (0 ≤ Tij  ≤ 1000)
### **출력**
모든 행성을 탐사하기 위한 최소 시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 0
0 30 1
1 0 29
28 1 0
```

**예제 출력1**

```
2
```

**예제 입력2**

```
4 1
0 83 38 7
15 0 30 83
67 99 0 44
14 46 81 0
```

**예제 출력2**

```
74
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(now, visited):
    if visited == (1 << N) - 1:
        return 0

    if dp[now][visited] != -1:
        return dp[now][visited]

    min_time = float('inf')
    for next in range(N):
        if not visited & (1 << next):
            time = graph[now][next] + dfs(next, visited | (1 << next))
            min_time = min(min_time, time)

    dp[now][visited] = min_time
    return min_time

print(dfs(K, 1 << K))

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111040|116|PyPy3|737
#### **📝해설**

**알고리즘**
```
1. 플로이드 워셜
2. 비트마스킹
3. DP
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline
INF = int(1e9)


def dfs(cur, visited, n, array, dp):
  # n개 행성 모두 방문
  if visited == (1 << n) - 1:
    return 0

  # 저장된 값이 존재
  if dp[cur][visited] != -1:
    return dp[cur][visited]

  dp[cur][visited] = INF
  
  # 지나가지 않은 경로로 지나감
  for i in range(n):
    # 방문한 곳은 스킵
    if visited & (1 << i):
      continue
    # 방문 안한 곳 방문
    dp[cur][visited] = min(dp[cur][visited], array[cur][i] + dfs(i, visited | (1 << i), n, array, dp))

  return dp[cur][visited]

def solution():
  n, k = map(int, input().split())
  array = [list(map(int, input().split())) for _ in range(n)]

  # 각 경로 최소 시간 구하기
  for x in range(n):
    for start in range(n):
      for end in range(n):
        if start == end:
          continue
        array[start][end] = min(array[start][end],
                                array[start][x] + array[x][end])

  # 각 방문 상태에 대한 최소 시간 저장
  dp = [[-1] * (1 << n) for _ in range(n)]

  print(dfs(k, 1 << k, n, array, dp))


if __name__ == '__main__':
  solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pjj21|32412|40|Python3|1146
#### **📝해설**

```python
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 플로이드 워셜 알고리즘을 통해 주어진 거리를 최단거리로 다시 저장
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# DP 배열을 통해 각 행성까지 도달한 거리를 저장
# dp[i][k] : k는 비트마스킹을 통해 지금까지 방문한 행성들을 저장. i번째 행성 방문
dp = [[-1] * (1 << N) for _ in range(N)]

# DFS를 통해 행성을 방문
def dfs(now, visited):

    # 모두 방문했다면 0리턴
    if visited == (1 << N) - 1:
        return 0

    # 이미 방문한 행성이라면 값을 리턴
    if dp[now][visited] != -1:
        return dp[now][visited]

    # 가능한 모든 행성을 방문하면서
    min_time = float('inf')
    for next in range(N):

        # 아직 방문하지 않았다면 방문처리
        if not visited & (1 << next):
            time = graph[now][next] + dfs(next, visited | (1 << next))
            min_time = min(min_time, time)

    # dp배열 갱신
    dp[now][visited] = min_time
    return min_time

print(dfs(K, 1 << K))

```