# [1600] 말이 되고픈 원숭이

### **난이도**
골드 3
## **📝문제**
동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그 녀석은 말(Horse)이 되기를 간절히 원했다. 그래서 그는 말의 움직임을 유심히 살펴보고 그대로 따라 하기로 하였다. 말은 말이다. 말은 격자판에서 체스의 나이트와 같은 이동방식을 가진다. 다음 그림에 말의 이동방법이 나타나있다. x표시한 곳으로 말이 갈 수 있다는 뜻이다. 참고로 말은 장애물을 뛰어넘을 수 있다.

```
 	x	 	x	 
x	 	 	 	x
 	 	말	 	 
x	 	 	 	x
 	x	 	x	
``` 
근데 원숭이는 한 가지 착각하고 있는 것이 있다. 말은 저렇게 움직일 수 있지만 원숭이는 능력이 부족해서 총 K번만 위와 같이 움직일 수 있고, 그 외에는 그냥 인접한 칸으로만 움직일 수 있다. 대각선 방향은 인접한 칸에 포함되지 않는다.

이제 원숭이는 머나먼 여행길을 떠난다. 격자판의 맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다. 인접한 네 방향으로 한 번 움직이는 것, 말의 움직임으로 한 번 움직이는 것, 모두 한 번의 동작으로 친다. 격자판이 주어졌을 때, 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법을 알아내는 프로그램을 작성하시오.
### **입력**
첫째 줄에 정수 K가 주어진다. 둘째 줄에 격자판의 가로길이 W, 세로길이 H가 주어진다. 그 다음 H줄에 걸쳐 W개의 숫자가 주어지는데, 0은 아무것도 없는 평지, 1은 장애물을 뜻한다. 장애물이 있는 곳으로는 이동할 수 없다. 시작점과 도착점은 항상 평지이다. W와 H는 1이상 200이하의 자연수이고, K는 0이상 30이하의 정수이다.
### **출력**
첫째 줄에 원숭이의 동작수의 최솟값을 출력한다. 시작점에서 도착점까지 갈 수 없는 경우엔 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
```

**예제 출력1**

```
4
```

**예제 입력2**

```
2
5 2
0 0 1 1 0
0 0 1 1 0
```

**예제 출력2**

```
-1
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

K = int(input())
W, H = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(H)]

q = deque()
q.append((0, 0, 0))
visited = [[[0] * W for _ in range(H)] for _ in range(K+1)]

jump = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y, current_jump = q.popleft()

    if x == H-1 and y == W-1:
        print(visited[current_jump][x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and table[nx][ny] == 0 and not visited[current_jump][nx][ny]:
            visited[current_jump][nx][ny] = visited[current_jump][x][y] + 1
            q.append((nx, ny, current_jump))
    

    if current_jump < K:
        for i in range(8):
            nx = x + jump[i][0]
            ny = y + jump[i][1]

            if 0 <= nx < H and 0 <= ny < W and table[nx][ny] == 0 and not visited[current_jump+1][nx][ny]:
                visited[current_jump+1][nx][ny] = visited[current_jump][x][y] + 1
                q.append((nx, ny, current_jump+1))
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|144364|532|PyPy3|1198
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
# BFS, 같은 횟수만큼 움직였을때 같은 위치에 도달했다면, 말 움직임이 적을 수록 유리하다.
import sys
from collections import deque
k = int(sys.stdin.readline())
w,h = map(int, sys.stdin.readline().split())
def my_conv(x):
    ret =[-1]*2
    for ob in x:
        if ob == '1':
            ret.append(-1)
        else:
            ret.append(0)
    ret.extend([-1]*2)
    return ret

def solution():
    visited =[[-1 for _ in range(w+4)] for _ in range(2)]
    visited.extend([my_conv(sys.stdin.readline().split()) for _ in range(h)])
    visited.extend([[-1 for _ in range(w+4)] for _ in range(2)])
    m_steps = ((1,0),(0,1),(0,-1),(-1,0))
    h_steps = ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))

    count = 0 # 몇번쨰 움직임인가
    q = deque([])
    q.append((2,2,1)) # 편의를 위해 1을 기본값으로 하자
    visited[2][2] = -1
    while q:
        for _ in range(len(q)):
            r,c,used_h= q.popleft()
            if r == h+1 and c == w+1:
                print(count)
                exit(0)
            if used_h < k + 1:             
                for h_step in h_steps:
                    nxt_r = r + h_step[0]
                    nxt_c = c + h_step[1]
                    if used_h + 1 < visited[nxt_r][nxt_c] or not visited[nxt_r][nxt_c]:
                        visited[nxt_r][nxt_c] = used_h + 1 
                        q.append((nxt_r,nxt_c,used_h + 1))
            for m_step in m_steps:
                nxt_r = r + m_step[0]
                nxt_c = c + m_step[1]
                if used_h < visited[nxt_r][nxt_c] or not visited[nxt_r][nxt_c]:
                    visited[nxt_r][nxt_c] = used_h
                    q.append((nxt_r,nxt_c,used_h))
        count += 1
    print(-1)
    return
solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
enigma_multi|135576|344|PyPy3|1792
#### **📝해설**

```python
from collections import deque
# 입력
K = int(input())
W, H = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(H)]

# BFS 사용을 위한 deque 선언과, 시작위치 삽입
q = deque()
q.append((0, 0, 0))
# 점프횟수마다 각기 다른 visited를 사용
visited = [[[0] * W for _ in range(H)] for _ in range(K+1)]

# 점프하는 이동을 위한 리스트
jump = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
]

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS 시작
while q:
    # 현재 위치와 현재 점프횟수를 queue에서 pop
    x, y, current_jump = q.popleft()

    # 도착점에 도착했다면, 그때 visited배열의 숫자를 출력
    if x == H-1 and y == W-1:
        print(visited[current_jump][x][y])
        break

    # 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스를 벗어나지 않고, 벽이 아니고, 방문하지 않았다면
        if 0 <= nx < H and 0 <= ny < W and table[nx][ny] == 0 and not visited[current_jump][nx][ny]:
            # 새롭게 방문한 곳에 visited 배열의 숫자를 1더해서 저장
            visited[current_jump][nx][ny] = visited[current_jump][x][y] + 1
            # queue에 push
            q.append((nx, ny, current_jump))
    

    # 아직 점프를 횟수만큼 다 하지 않은 상태라면
    if current_jump < K:
        # 점프를 함
        for i in range(8):
            nx = x + jump[i][0]
            ny = y + jump[i][1]
            # 인덱스를 벗어나지 않고 ...
            if 0 <= nx < H and 0 <= ny < W and table[nx][ny] == 0 and not visited[current_jump+1][nx][ny]:
                # 점프횟수를 1 더한 visited 배열에 값을 갱신
                visited[current_jump+1][nx][ny] = visited[current_jump][x][y] + 1
                q.append((nx, ny, current_jump+1))
# q가 빌 때까지 도착하지 못했다면 -1 출력
else:
    print(-1)
```