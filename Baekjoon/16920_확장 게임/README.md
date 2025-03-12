# [16920] 확장 게임

### **난이도**
골드 2
## **📝문제**
구사과와 친구들이 확장 게임을 하려고 한다. 이 게임은 크기가 N×M인 격자판 위에서 진행되며, 각 칸은 비어있거나 막혀있다. 각 플레이어는 하나 이상의 성을 가지고 있고, 이 성도 격자판 위에 있다. 한 칸 위에 성이 두 개 이상인 경우는 없다.

게임은 라운드로 이루어져 있고, 각 라운드마다 플레이어는 자기 턴이 돌아올 때마다 성을 확장해야 한다. 제일 먼저 플레이어 1이 확장을 하고, 그 다음 플레이어 2가 확장을 하고, 이런 식으로 라운드가 진행된다.

각 턴이 돌아왔을 때, 플레이어는 자신이 가지고 있는 성을 비어있는 칸으로 확장한다. 플레이어 i는 자신의 성이 있는 곳에서 Si칸 만큼 이동할 수 있는 모든 칸에 성을 동시에 만든다. 위, 왼쪽, 오른쪽, 아래로 인접한 칸으로만 이동할 수 있으며, 벽이나 다른 플레이어의 성이 있는 곳으로는 이동할 수 없다. 성을 다 건설한 이후엔 다음 플레이어가 턴을 갖는다.

모든 플레이어가 더 이상 확장을 할 수 없을 때 게임이 끝난다. 게임판의 초기 상태가 주어졌을 때, 최종 상태를 구해보자.
### **입력**
첫째 줄에 격자판의 크기 N, M과 플레이어의 수 P가 주어진다. 둘째 줄에는 S1, S2, ...SP가 주어진다.

다음 N개의 줄에는 게임판의 상태가 주어진다. '.'는 빈 칸, '#'는 벽, '1', '2', ..., '9'는 각 플레이어의 성이다.

모든 플레이어는 적어도 하나의 성을 가지고 있으며, 게임에 참가하지 않는 플레이어의 성이 있는 경우는 없다.

- 1 ≤ N, M ≤ 1,000
- 1 ≤ P ≤ 9
- 1 ≤ Si ≤ 109
### **출력**
플레이어 1이 가진 성의 수, 2가 가진 성의 수, ..., P가 가진 성의 수를 공백으로 구분해 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3 2
1 1
1..
...
..2
```

**예제 출력1**

```
6 3
```

**예제 입력2**

```
3 3 2
1 1
1.1
...
..2
```

**예제 출력2**

```
7 2
```

**예제 입력3**

```
4 4 2
1 1
1...
....
....
...2
```

**예제 출력3**

```
10 6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M, P = map(int, input().split())
move_dist = [0] + list(map(int, input().split()))

table = [list(input().strip()) for _ in range(N)]
castles = [deque() for _ in range(P+1)]

for i in range(N):
    for j in range(M):
        if table[i][j] not in  [".", "#"]:
            castles[int(table[i][j])].append((i,j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while any(castles[i] for i in range(1, P+1)):
    for player in range(1, P+1):
        if not castles[player]:
            continue

        q = castles[player]
        steps = move_dist[player]
        new_castles = deque()

        for _ in range(steps):
            if not q:
                break

            for _ in range(len(q)):
                x, y = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == ".":
                        table[nx][ny] = str(player)
                        new_castles.append((nx, ny))

            q.extend(new_castles)
            new_castles.clear()

result = [0] * (P+1)
for i in range(N):
    for j in range(M):
        if table[i][j].isdigit():
            result[int(table[i][j])] += 1

print(" ".join(map(str, result[1:])))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|198024|548|PyPy3|1273
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
from collections import deque
import sys

input = sys.stdin.readline
N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
visited = [[0] * M for _ in range(N)]
result = [0] * (P + 1)
Q = [deque([]) for _ in range(10)]

for n in range(N):
    temp = list(input())
    for m in range(M):
        if temp[m] == '#':
            visited[n][m] = 1
        elif temp[m] != '.':
            visited[n][m] = 1
            result[int(temp[m])] += 1
            Q[int(temp[m])].append((n, m))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while 1:
    flag = 1
    for p in range(1, P + 1):
        for _ in range(min(S[p], max(N, M))):
            for _ in range(len(Q[p])):
                x, y = Q[p].popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        result[p] += 1
                        Q[p].append((nx, ny))
                        flag = 0
    if flag:
        break
print(' '.join(map(str, result[1:])))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dhkimxx|154616|360|PyPy3|1111
#### **📝해설**

```python
from collections import deque

# 입력받기
N, M, P = map(int, input().split())
move_dist = [0] + list(map(int, input().split()))

table = [list(input().strip()) for _ in range(N)]

# 각 플레이어마다 갖고 있는 성의 좌표를 deque로 저장
castles = [deque() for _ in range(P+1)]

# 초기 정보 삽입
for i in range(N):
    for j in range(M):
        if table[i][j] not in  [".", "#"]:
            castles[int(table[i][j])].append((i,j))

# 상하좌우 이동을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 더이상 새로 지을 수 있는 성이 없을때까지 반복
while any(castles[i] for i in range(1, P+1)):
    for player in range(1, P+1):

        # 새로 지을 성이 없는 플레이어라면 넘어감
        if not castles[player]:
            continue
        
        # 이번 플레이어가 갖고 있는 성의 위치 큐
        q = castles[player]

        # 플레이어의 이동 거리
        steps = move_dist[player]

        # 이번 라운드에 새로 지을 성 큐
        new_castles = deque()

        # 주어진 이동거리만큼 반복
        for _ in range(steps):

            # 큐가 비었다면 종료
            if not q:
                break
            
            # 큐에 있는 모든 원소를 검사
            for _ in range(len(q)):
                x, y = q.popleft()

                # 상하좌우 네방향 탐색
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    # 새롭게 성을 추가
                    if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == ".":
                        table[nx][ny] = str(player)
                        new_castles.append((nx, ny))

            q.extend(new_castles)
            new_castles.clear()

result = [0] * (P+1)
for i in range(N):
    for j in range(M):
        if table[i][j].isdigit():
            result[int(table[i][j])] += 1

print(" ".join(map(str, result[1:])))
```