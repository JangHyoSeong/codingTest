# [21610] 마법사 상어와 비바라기

### **난이도**
골드 5
## **📝문제**

### **입력**

### **출력**

### **예제입출력**

**예제 입력1**

```
```

**예제 출력1**

```
```

**예제 입력2**

```
```

**예제 출력2**

```
```

**예제 입력3**

```
```

**예제 출력3**

```
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
bucket = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]


visited = [[False] * N for _ in range(N)]

for command in range(M):
    dir, length = commands[command]
    
    clouds = []
    
    if command == 0:
        clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

        
    else:
        for i in range(N):
            for j in range(N):
                if bucket[i][j] >= 2 and not visited[i][j]:
                    clouds.append([i, j])
                    bucket[i][j] -= 2

    visited = [[False] * N for _ in range(N)]

    clouds_num = len(clouds)
    clouds_moving = []
    for idx in range(clouds_num):
        nx = clouds[idx][0] + dx[dir] * length
        ny = clouds[idx][1] + dy[dir] * length
        
        nx %= N
        ny %= N
        
        bucket[nx][ny] += 1
        
        visited[nx][ny] = True
        clouds_moving.append((nx, ny))
    
    for idx in range(clouds_num):
        x, y = clouds_moving[idx]
        
        for i in [-1, 1]:
            for j in [-1, 1]:
                if 0 <= x+i < N and 0 <= y+j < N and bucket[x+i][y+j] > 0:
                    bucket[x][y] += 1
                    
water_sum = 0
for i in range(N):
    for j in range(N):
        if bucket[i][j] >= 2 and not visited[i][j]:
            bucket[i][j] -= 2
        
        water_sum += bucket[i][j]
        
print(water_sum)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|113676|180|PyPy3|1522|
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
# 마법사 상어와 비바라기
import sys


def process1(command):
    global N, cloud
    for i in range(0, len(cloud)):
        x, y = cloud[i]
        dx, dy = command
        x, y = (x + dx) % N, (y + dy) % N
        cloud[i] = (x, y)


def process2():
    global A, cloud, prev_increase
    for x, y in cloud:
        A[x][y] += 1
        prev_increase[x][y] = True


def process3():
    global cloud, prev_cloud
    prev_cloud = cloud
    cloud = []


def process4():
    global prev_cloud, diagonals, N, A
    for i, j in prev_cloud:
        cnt = 0
        for dx, dy in diagonals:
            x, y = i + dx, j + dy
            if 0 <= x < N and 0 <= y < N:
                if A[x][y] > 0:
                    cnt += 1
        A[i][j] += cnt


def process5():
    global A, N, cloud, prev_increase
    for x in range(N):
        for y in range(N):
            if A[x][y] >= 2 and not prev_increase[x][y]:
                A[x][y] -= 2
                cloud.append((x, y))
            prev_increase[x][y] = False


def process(command):
    process1(command)
    process2()
    process3()
    process4()
    process5()


input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
commands = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diagonals = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
prev_increase = [[False for _ in range(N)] for _ in range(N)]
prev_cloud = []
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for _ in range(M):
    D, S = map(int, input().split())
    tmp_command = commands[D - 1]
    tmp_command = (tmp_command[0] * S, tmp_command[1] * S)
    process(tmp_command)
print(sum([sum(A[i]) for i in range(N)]))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
wjdac66|111848|145|PyPy3|1746
#### **📝해설**

```python
N, M = map(int, input().split())
bucket = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]

# 구름을 이동하기 위한 리스트
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 이전 이동에서 구름의 생성 여부를 검사할 visited 리스트
visited = [[False] * N for _ in range(N)]

for command in range(M):
    # 이동방향, 길이 저장
    dir, length = commands[command]
    
    # 이번 이동에서의 구름의 위치를 저장할 리스트
    clouds = []
    
    # 첫 번째 이동이라면 구름의 위치는 고정
    if command == 0:
        clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

    # 첫 번째 이동이 아니라면 물의 양이 2이상인 위치 + 이전에 구름이 생기지 않았던 위치
    else:
        for i in range(N):
            for j in range(N):
                if bucket[i][j] >= 2 and not visited[i][j]:
                    clouds.append([i, j])
                    bucket[i][j] -= 2

    # visited 리스트는 다시 처음으로 돌려줌
    visited = [[False] * N for _ in range(N)]

    clouds_num = len(clouds)
    clouds_moving = []

    # 구름의 위치를 순회하며 이동, 물의 양 더하기, 방문처리를 해줌
    for idx in range(clouds_num):
        nx = clouds[idx][0] + dx[dir] * length
        ny = clouds[idx][1] + dy[dir] * length
        
        nx %= N
        ny %= N
        
        bucket[nx][ny] += 1
        
        visited[nx][ny] = True
        clouds_moving.append((nx, ny))
    
    # 새롭게 이동한 위치에서 대각선을 검사하여 물 추가
    for idx in range(clouds_num):
        x, y = clouds_moving[idx]
        
        for i in [-1, 1]:
            for j in [-1, 1]:
                if 0 <= x+i < N and 0 <= y+j < N and bucket[x+i][y+j] > 0:
                    bucket[x][y] += 1

# 모든 이동이 끝난 후 물의 양 계산         
water_sum = 0
for i in range(N):
    for j in range(N):
        if bucket[i][j] >= 2 and not visited[i][j]:
            bucket[i][j] -= 2
        
        water_sum += bucket[i][j]
        
print(water_sum)
```

### **🔖정리**

1. 배운점