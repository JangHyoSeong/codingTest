# [1937] 욕심쟁이 판다

### **난이도**
골드 3
## **📝문제**
n × n의 크기의 대나무 숲이 있다. 욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다. 그리고 그 곳의 대나무를 다 먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다. 그리고 또 그곳에서 대나무를 먹는다. 그런데 단 조건이 있다. 이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.

이 판다의 사육사는 이런 판다를 대나무 숲에 풀어 놓아야 하는데, 어떤 지점에 처음에 풀어 놓아야 하고, 어떤 곳으로 이동을 시켜야 판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다. 우리의 임무는 이 사육사를 도와주는 것이다. n × n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.
### **입력**
첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다. 그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어진다. 대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다. 대나무의 양은 1,000,000보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에는 판다가 이동할 수 있는 칸의 수의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline().rstrip())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] > table[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        
    
    return dp[x][y]

result = 0
for i in range(N):
    for j in range(N):
        result = max(result, dfs(i, j))

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|52296|1036|Python3|642
#### **📝해설**

**알고리즘**
```
1. DP
2. DFS
```

### **다른 풀이**

```python
def dfs(i,j):
    if dp[i][j]!=-1:
        return dp[i][j]

    dp[i][j]=0
    
    for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] > arr[i][j]:
            dp[i][j] = max(dp[i][j], 1+dfs(ni,nj))

    return dp[i][j]


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(N):
        dp[i][j] = dfs(i,j)
        ans = max(ans, dp[i][j])
print(ans+1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
smpa6379|138680|260|PyPy3
#### **📝해설**

```python
import sys
sys.setrecursionlimit(1000000)

# 입력받기
N = int(sys.stdin.readline().rstrip())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# DP배열. i, j에서 시작할 때 최대 이동 거리
dp = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# DFS
def dfs(x, y):

    # 이미 값이 있는 곳에 방문한다면 그 값을 리턴
    if dp[x][y]:
        return dp[x][y]


    # 방문 처리
    dp[x][y] = 1

    # 상하좌우를 탐색하면서
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 이동가능한 위치라면
        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] > table[x][y]:

            # 이동 후, 현재값이 크다면 유지, 이동한 값이 크다면 변경
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        
    # 현재 값을 리턴
    return dp[x][y]

# DP배열중 가장 큰 값을 출력
result = 0
for i in range(N):
    for j in range(N):
        result = max(result, dfs(i, j))

print(result)
```