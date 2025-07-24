# [1405] 미친 로봇

### **난이도**
골드 4
## **📝문제**
통제 할 수 없는 미친 로봇이 평면위에 있다. 그리고 이 로봇은 N번의 행동을 취할 것이다.

각 행동에서 로봇은 4개의 방향 중에 하나를 임의로 선택한다. 그리고 그 방향으로 한 칸 이동한다.

로봇이 같은 곳을 한 번보다 많이 이동하지 않을 때, 로봇의 이동 경로가 단순하다고 한다. (로봇이 시작하는 위치가 처음 방문한 곳이다.) 로봇의 이동 경로가 단순할 확률을 구하는 프로그램을 작성하시오. 예를 들어, EENE와 ENW는 단순하지만, ENWS와 WWWWSNE는 단순하지 않다. (E는 동, W는 서, N은 북, S는 남)
### **입력**
첫째 줄에 N, 동쪽으로 이동할 확률, 서쪽으로 이동할 확률, 남쪽으로 이동할 확률, 북쪽으로 이동할 확률이 주어진다. N은 14보다 작거나 같은 자연수이고,  모든 확률은 100보다 작거나 같은 자연수 또는 0이다. 그리고, 동서남북으로 이동할 확률을 모두 더하면 100이다.

확률의 단위는 %이다.
### **출력**
첫째 줄에 로봇의 이동 경로가 단순할 확률을 출력한다. 절대/상대 오차는 10-9 까지 허용한다.
### **예제입출력**

**예제 입력1**

```
2 25 25 25 25
```

**예제 출력1**

```
0.75
```

**예제 입력2**

```
1 25 25 25 25
```

**예제 출력2**

```
1.0
```

**예제 입력3**

```
7 50 0 0 50
```

**예제 출력3**

```
1.0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, east, west, south, north = map(int, input().split())

probs = [east, west, south, north]
probs = [p / 100 for p in probs]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * (2 * N + 1) for _ in range(2 * N + 1)]
start_x, start_y = N, N

result = 0

def dfs(x, y, depth, prob):
    global result

    if depth == N:
        result += prob
        return
    
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if not visited[nx][ny] and probs[d] > 0:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, prob * probs[d])
            visited[nx][ny] = False
    
visited[start_x][start_y] = True
dfs(start_x, start_y, 0, 1.0)

print(f"{result:.10f}")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|113336|392|PyPy3|696
#### **📝해설**

**알고리즘**
```
1. 백트래킹
2. DFS
```

### **다른 풀이**

```python
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dfs(x, y, cnt, p):
    global ans

    if cnt == n:
        ans += p
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if board[nx][ny]:
            continue
        if not 0 <= nx < (2 * n) + 1 or not 0 <= ny < (2 * n) + 1:
            continue

        board[nx][ny] = 1
        dfs(nx, ny, cnt + 1, p * poss[i] * 0.01)
        board[nx][ny] = 0


n, east, west, south, north = map(int, input().split())
poss = [north, east, south, west]   

board = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
board[n][n] = 1

ans = 0

dfs(n, n, 0, 1)
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
yj0624|113184|376|PyPy3|630
#### **📝해설**

```python
N, east, west, south, north = map(int, input().split())

# 이동할 확률
probs = [east, west, south, north]
probs = [p / 100 for p in probs]

# 동 서 남 북 순서대로 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부를 저장하기 위해 이차원 리스트 설정
visited = [[False] * (2 * N + 1) for _ in range(2 * N + 1)]

# 시작지점
start_x, start_y = N, N

result = 0

# 재귀함수
def dfs(x, y, depth, prob):
    global result

    # N번 이동했다면
    if depth == N:

        # 그때까지의 확률을 결과에 더함
        result += prob
        return
    
    # 동서남북으로 이동하면서
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        # 한번도 방문하지 않았던 곳만 방문
        if not visited[nx][ny] and probs[d] > 0:

            # 백트래킹
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, prob * probs[d])
            visited[nx][ny] = False

# DFS 시작
visited[start_x][start_y] = True
dfs(start_x, start_y, 0, 1.0)

print(f"{result:.10f}")
```