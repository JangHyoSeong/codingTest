# [27737] 버섯 농장

### **난이도**
실버 1
## **📝문제**
농부 해강이는 
$N \times N$ 칸으로 이루어진 나무판에서 버섯 농사를 짓는다. 나무판은 버섯이 자랄 수 있는 칸과 없는 칸으로 이루어져 있다.

해강이는 
$M$개의 버섯 포자를 가지고 있다. 버섯 포자는 버섯이 자랄 수 있는 칸에만 심을 수 있다.

각 버섯 포자는 포자가 심어진 칸을 포함해 최대 
$K$개의 연결된 (버섯이 자랄 수 있는) 칸에 버섯을 자라게 한다. 이때 연결된 칸은 상하좌우로 적어도 한 변을 공유하는 칸들의 집합이라고 정의한다.

또한 한 칸에 버섯 포자를 여러 개 겹쳐서 심을 수 있으며, 만약 
$x$개의 버섯 포자를 겹쳐 심으면 포자가 심어진 칸을 포함해 최대 
$x \times K$개의 연결된 (버섯이 자랄 수 있는) 칸에 버섯이 자란다.

![이미지](https://upload.acmicpc.net/d6cf1de2-1a5a-4185-bb45-bc37eb4e4476/-/preview/)

<그림 1> 
$K = 4$일 때 버섯이 자라는 모습이다.

![이미지](https://upload.acmicpc.net/239f2d7b-7589-4f72-9088-993428eb234a/-/preview/)

<그림 2> 
$K = 10$일 때 버섯이 자라는 모습이다.

해강이는 버섯 포자를 심을 때 최소 개수로만 심으려고 한다. 해강이가 농사가 가능할지 판단하고, 농사가 가능하다면 남은 버섯 포자의 개수를 출력하시오.

버섯 포자를 하나라도 사용하고 버섯이 자랄 수 있는 모든 칸에 버섯이 전부 자랐을 때 농사가 가능하다고 정의한다.
### **입력**
첫 번째 줄에 
$N$, 
$M$, 
$K$가 공백으로 구분되어 주어진다.

두 번째 줄부터 
$N$개의 줄에 나무판의 각 칸의 상태가 공백으로 구분되어 주어진다.

버섯이 자랄 수 있는 칸은 0, 버섯이 자랄 수 없는 칸은 1로 주어진다.
### **출력**
만약 버섯 농사가 불가능하면 IMPOSSIBLE을 출력한다.

버섯 농사가 가능하다면, POSSIBLE을 출력하고 다음 줄에 남은 버섯 포자의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 100 1
1 1 1 0 0
1 0 1 0 0
0 0 1 1 1
1 1 0 0 0
0 1 1 0 1
```

**예제 출력1**

```
POSSIBLE
88
```

**예제 입력2**

```
5 5 1
1 1 1 0 0
1 0 1 0 0
0 0 1 1 1
1 1 0 0 0
0 1 1 0 1
```

**예제 출력2**

```
IMPOSSIBLE
```

**예제 입력3**

```
5 100 3
1 1 1 0 0
1 0 1 0 0
0 0 1 1 1
1 1 0 0 0
0 1 1 0 1
```

**예제 출력3**

```
POSSIBLE
94
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

spore = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] or table[i][j] == 1:
            continue

        q = deque([(i, j)])
        visited[i][j] = True

        now_area = 1
        while q:
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    now_area += 1
        
        if now_area % K:
            spore = spore + (now_area // K) + 1
        else:
            spore += now_area // K

if spore <= M and spore != 0:
    print("POSSIBLE")
    print(M - spore)
else:
    print("IMPOSSIBLE")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34984|80|Python3|980
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

N, M, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 방문 여부 저장
visited = [[False] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 현재까지 사용한 포자의 개수
spore = 0

# 모든 지점을 탐색하면서
for i in range(N):
    for j in range(N):

        # 이미 방문했거나, 포자가 존재하지 못하는 지역이면 넘어감
        if visited[i][j] or table[i][j] == 1:
            continue
        
        # 현재 위치부터 BFS 시작
        q = deque([(i, j)])
        visited[i][j] = True

        # 현재 영역의 넓이
        now_area = 1

        # BFS 탐색
        while q:
            x, y = q.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    now_area += 1
        # 현재 영역이 K개로 나누어 떨어지지 않는다면
        if now_area % K:

            # 포자 사용(올림)
            spore = spore + (now_area // K) + 1

        # 딱 나누어 떨어진다면 그 만큼만 포자 사용
        else:
            spore += now_area // K

# 포자 사용을 M개보다 적게 하고, 하나 이상 사용한 경우
if spore <= M and spore != 0:
    print("POSSIBLE")
    print(M - spore)
# 불가능한 경우
else:
    print("IMPOSSIBLE")
```