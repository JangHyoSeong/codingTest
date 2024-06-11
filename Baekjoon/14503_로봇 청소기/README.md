# [14503] 로봇 청소기

### **난이도**
골드 5
## **📝문제**
로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 방은 
$N \times M$ 크기의 직사각형으로 나타낼 수 있으며, 
$1 \times 1$ 크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다. 방의 각 칸은 좌표 
$(r, c)$로 나타낼 수 있고, 가장 북쪽 줄의 가장 서쪽 칸의 좌표가 
$(0, 0)$, 가장 남쪽 줄의 가장 동쪽 칸의 좌표가 
$(N-1, M-1)$이다. 즉, 좌표 
$(r, c)$는 북쪽에서 
$(r+1)$번째에 있는 줄의 서쪽에서 
$(c+1)$번째 칸을 가리킨다. 처음에 빈 칸은 전부 청소되지 않은 상태이다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
   1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
   2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
   1. 반시계 방향으로 $90^\circ$ 회전한다.
   2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
   3. 1번으로 돌아간다.

### **입력**
첫째 줄에 방의 크기 
$N$과 
$M$이 입력된다. 
$(3 \le N, M \le 50)$  둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표 
$(r, c)$와 처음에 로봇 청소기가 바라보는 방향 
$d$가 입력된다. 
$d$가 
$0$인 경우 북쪽, 
$1$인 경우 동쪽, 
$2$인 경우 남쪽, 
$3$인 경우 서쪽을 바라보고 있는 것이다.

셋째 줄부터 
$N$개의 줄에 각 장소의 상태를 나타내는 
$N \times M$개의 값이 한 줄에 
$M$개씩 입력된다. 
$i$번째 줄의 
$j$번째 값은 칸 
$(i, j)$의 상태를 나타내며, 이 값이 
$0$인 경우 
$(i, j)$가 청소되지 않은 빈 칸이고, 
$1$인 경우 
$(i, j)$에 벽이 있는 것이다. 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다. 로봇 청소기가 있는 칸은 항상 빈 칸이다.
### **출력**
로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
1 1 0
1 1 1
1 0 1
1 1 1
```

**예제 출력1**

```
1
```

**예제 입력2**

```
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
```

**예제 출력2**

```
57
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
x, y, dir = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    can_clean = False
    if table[x][y] == 0:
        table[x][y] = 2
        count += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0:
            can_clean = True
            break

    if can_clean:
        while True:
            dir = (dir - 1) % 4
            nx = x + direction[dir][0]
            ny = y + direction[dir][1]

            if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0:
                x = nx
                y = ny
                break
    else:
        nx = x - direction[dir][0]
        ny = y - direction[dir][1]

        if 0 <= nx < N and 0 <= ny < M and table[nx][ny] != 1:
            x = nx
            y = ny
        else:
            break

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|44|Python3|1028
#### **📝해설**

**알고리즘**
```
1. 구현
```
#### **📝해설**

```python
N, M = map(int, input().split())
x, y, dir = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 입력받고 방향을 정의해둠

# 상하좌우를 탐색하기 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 몇 칸을 청소했는지 셈
count = 0

# break를 만날 때까지 반복
while True:
    # 주위 4방향이 청소 가능한지 여부를 파악할 변수
    can_clean = False
    # 현재 칸이 청소가능하다면 청소 후, 다시 청소하지 않게 값을 변경
    if table[x][y] == 0:
        table[x][y] = 2
        count += 1
    
    # 상하좌우 4방향을 탐색하면서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스를 벗어나지 않고 빈공간이 있다면
        if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0:
            # 청소가능여부를 True로 바꾸고 탐색종료
            can_clean = True
            break
        
    # 청소가능한 칸이 있다면
    if can_clean:
        # 반시계 방향으로 회전하면서 청소 가능한 칸을 찾음
        while True:
            dir = (dir - 1) % 4
            nx = x + direction[dir][0]
            ny = y + direction[dir][1]

            # 청소가능한 칸으로 이동
            if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0:
                x = nx
                y = ny
                break
    # 청소가능한칸이 없다면
    else:
        # 현재 방향의 뒤쪽으로 이동
        nx = x - direction[dir][0]
        ny = y - direction[dir][1]
        # 인덱스를 벗어나지 않고 벽이 아니라면 이동
        if 0 <= nx < N and 0 <= ny < M and table[nx][ny] != 1:
            x = nx
            y = ny
        # 인덱스를 벗어나거나 벽을 만난다면 종료
        else:
            break

print(count)
```