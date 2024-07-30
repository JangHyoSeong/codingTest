# [14442] 벽 부수고 이동하기 2

### **난이도**
골드 3
## **📝문제**
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000), K(1 ≤ K ≤ 10)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
### **출력**
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

### **예제입출력**

**예제 입력1**

```
6 4 1
0100
1110
1000
0000
0111
0000
```

**예제 출력1**

```
15
```

**예제 입력2**

```
6 4 2
0100
1110
1000
0000
0111
0000
```

**예제 출력2**

```
9
```

**예제 입력3**

```
4 4 3
0111
1111
1111
1110
```

**예제 출력3**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

# 입력받음
N, M, K = map(int, input().split())
table = [list(map(int, input())) for _ in range(N)]

# 각 벽 부순 횟수마다 visited배열을 만들어줌
visited = [[[False] * M for _ in range(N)] for _ in range(K+1)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 선언
visited[0][0][0] = True
q = deque([[0, 0, 0, 1]])

# 도달하지 못한다면 flag = False
flag = False

# BFS
while q:

    # popleft
    x, y, wall_count, dis = q.popleft()

    # 도착지에 도착했다면 break
    if x == N-1 and y == M-1:
        flag = True
        break

    # 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스를 벗어나지 않는지 검사
        if 0 <= nx < N and 0 <= ny < M:
            
            # 벽 부수는 횟수가 남아있고, 벽을 만났고, 방문한적 없는 케이스라면 방문
            if wall_count < K and table[nx][ny] == 1 and not visited[wall_count+1][nx][ny]:
                visited[wall_count+1][nx][ny] = True
                q.append([nx, ny, wall_count+1, dis+1])

            # 벽을 부수지 않고, 아직 방문하지 않은 케이스라면 방문
            if table[nx][ny] == 0 and not visited[wall_count][nx][ny]:
                visited[wall_count][nx][ny] = True
                q.append([nx, ny, wall_count, dis+1])


# 출력
if flag:
    print(dis)
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|318532|4592|PyPy3|953
#### **📝해설**

**알고리즘**
```
1. BFS
```