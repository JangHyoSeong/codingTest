# [1520] 내리막 길

### **난이도**
골드 3
## **📝문제**
여행을 떠난 세준이는 지도를 하나 구하였다. 이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.

현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다. 그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다. 위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.

지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다. 이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다. M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.
### **출력**
첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.
### **예제입출력**

**예제 입력1**

```
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
```

**예제 출력1**

```
3
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
# 입력 처리
M, N = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(M)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and heights[nx][ny] < heights[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

# 경로의 수 계산 및 출력
print(dfs(0, 0))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|42796|168|Python3|568
#### **📝해설**

**알고리즘**
```
1. DFS
2. DP
```

### **다른 풀이**

```python
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(sx, sy):
    # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if sx == m-1 and sy == n-1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[sx][sy] != -1:
        return dp[sx][sy]
    
    ways = 0
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[sx][sy] > graph[nx][ny]:
            ways += dfs(nx, ny)
    
    dp[sx][sy] = ways
    return dp[sx][sy]


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

print(dfs(0,0))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
junha06|42780|112|Python3|769
#### **📝해설**

```python
# 입력 처리
M, N = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(M)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 이미 방문한 지점을 표시하기 위한 리스트
dp = [[-1] * N for _ in range(M)]

# DFS 함수
def dfs(x, y):

    # 목적지에 도달했다면 1 리턴
    if x == M-1 and y == N-1:
        return 1

    # 이미 방문한 목적지라면 방문x
    if dp[x][y] != -1:
        return dp[x][y]

    # 방문하지 않은 목적지라면 방문처리를 함
    dp[x][y] = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 인덱스를 비교하고, 더 낮은곳이라면 이동
        if 0 <= nx < M and 0 <= ny < N and heights[nx][ny] < heights[x][y]:
            # 방문 횟수를 dp에 저장
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

# 경로의 수 계산 및 출력
print(dfs(0, 0))
```

### **🔖정리**

1. 배운점