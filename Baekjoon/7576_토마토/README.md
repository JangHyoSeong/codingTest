# [7576] 토마토

### **난이도**
골드 5
## **📝문제**
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.



창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
### **입력**
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.
### **출력**
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

### **예제입출력**

**예제 입력1**

```
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
```

**예제 출력1**

```
8
```

**예제 입력2**

```
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
```

**예제 출력2**

```
-1
```

**예제 입력3**

```
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
```

**예제 출력3**

```
6
```

### **출처**
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2013 > 고등부 1번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

width, height = map(int, input().split())

# 큐를 두개 선언
q1 = deque()
q2 = deque()
tomatoes = []

# 익지않은 토마토의 개수
not_tomato_num = 0
# 토마토를 입력받음
for i in range(height):
    one_line = list(map(int, input().split()))
    tomatoes.append(one_line)
    for j in range(width):
        if one_line[j] == 1:
            q1.append([i, j])
        # 익지않은 토마토의 개수를 저장
        elif one_line[j] == 0:
            not_tomato_num += 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

day = 0

# queue가 빌 때까지 BFS
while q1 or q2:

    # q1과 q2를 번갈아가면서 사용
    # 이를 통해 날짜가 며칠 지났는지 확인 가능
    while q1:
        now_x, now_y = q1.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if 0 <= next_x < height and 0 <= next_y < width and tomatoes[next_x][next_y] == 0:
                q2.append([next_x, next_y])
                tomatoes[next_x][next_y] = 1
                not_tomato_num -= 1
    
    if q2 != deque():
        day += 1
    

    while q2:
        now_x, now_y = q2.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if 0 <= next_x < height and 0 <= next_y < width and tomatoes[next_x][next_y] == 0:
                q1.append([next_x, next_y])
                tomatoes[next_x][next_y] = 1
                not_tomato_num -= 1

    if q1 != deque():
        day += 1
# 익지않은 토마토의 개수가 0이 아니라면 -1출력
if not_tomato_num:
    print(-1)
else:
    print(day)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|213116|444|PyPy3|1330
#### **📝해설**

**알고리즘**
```
1.BFS(너비 우선 탐색)
2.queue
```

### **다른 풀이**

```python
import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

M, N = map(int, input().split())
arr = [[-1] * (M + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (M + 2)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = []
ans = -1
cnt = 0

for i in range(1, N + 1):
	for j in range(1, M + 1):
		if arr[i][j] == 0:
			cnt += 1
		elif arr[i][j] == 1:
			q.append((i, j))

while q:
	new_q = []
	for i, j in q:
		for dy, dx in d:
			y, x = i + dy, j + dx
			if arr[y][x] == 0:
				cnt -= 1
				arr[y][x] = 1
				new_q.append((y, x))
	q = new_q
	ans += 1

print(ans if cnt == 0 else -1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rhaxhdals|181344|304|PyPy3|625
#### **📝해설**
비슷한 방식이지만, 굳이 pop, deque를 사용하지 않고 간결하게 풀었다

### **🔖정리**

1. BFS 사용법