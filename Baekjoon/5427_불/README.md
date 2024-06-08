# [5427] 불

### **난이도**
골드 4
## **📝문제**
상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.

매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.

각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)

다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

- '.': 빈 공간
- '#': 벽
- '@': 상근이의 시작 위치
- '*': 불  
각 지도에 @의 개수는 하나이다.
### **출력**
각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###
```

**예제 출력1**

```
2
5
IMPOSSIBLE
IMPOSSIBLE
IMPOSSIBLE
```

### **출처**
ICPC > Regionals > Europe > Northwestern European Regional Contest > Benelux Algorithm Programming Contest > BAPC 2012 F번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

T = int(input())

def find_start():
    # 시작 지점을 찾는 함수
    for i in range(N):
        for j in range(M):
            if table[i][j] == '@':
                table[i][j] = '.'
                return (i, j)

for testcase in range(T):
    # 입력받기
    M, N = map(int, input().split())
    table = [list(input()) for _ in range(N)]

    # 방문 여부를 처리할 리스트
    visited = [[False] * M for _ in range(N)]

    # 현재 상근이가 있을 수 있는 좌표들을 담은 deque(큐)
    now_q = deque()
    # 시작 위치를 저장
    start = find_start()
    # 시작 위치 방문 처리
    visited[start[0]][start[1]] = True
    # 시작 위치를 삽입후 시작
    now_q.append(start)

    # 탈출여부, 불가능 여부를 변수에 저장
    escape = False
    impossible = False

    # 상하좌우 탐색을 위한 리스트
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 몇초가 지났는지 저장할 변수
    count = 0

    # 현재 불의 위치를 저장할 리스트
    now_fire = []
    # 현재 불의 위치를 리스트에 저장
    for i in range(N):
        for j in range(M):
            if table[i][j] == '*':
                now_fire.append((i, j))

    # 탈출했거나, 탈출 못하는 경우 반복 종료
    while not escape and not impossible:

        next_fire = []
        
        for fire in now_fire:
            for i in range(4):
                nx = fire[0] + dx[i]
                ny = fire[1] + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if table[nx][ny] == '.':
                        table[nx][ny] = '*'
                        next_fire.append((nx, ny))
        
        now_fire = next_fire

        next_queue = deque()

        while now_q:
            now = now_q.popleft()

            for i in range(4):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny] and table[nx][ny] == '.':
                        next_queue.append((nx, ny))
                        visited[nx][ny] = True
                else:
                    escape = True

        if next_queue == deque():
            impossible = True
        else:
            now_q = next_queue

        count += 1
         
    if escape == True:
        print(count)
    else:
        print('IMPOSSIBLE')
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|237896|856|PyPy3|2440
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **😅개선점**
처음에 모든 불에 대해서 상하좌우 탐색을 진행한 후, 새로운 불을 옮겨주었다. 이런 방식을 사용하다 보니, 모든 불을 탐색하는 것이 오래 걸렸고, 새롭게 옮겨준 불 만이 다시 옆으로 불을 옮겨줄 수 있다는 것을 알게 되어 방식을 바꾸어 통과했다.

### **다른 풀이**

```python
import io, os, sys


def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    for _ in range(int(input())):
        cols, rows = map(int, input().split())
        board = [list(input().rstrip()) for _ in range(rows)]
        answer = problem(rows, cols, board)
        if answer == -1:
            print("IMPOSSIBLE")
        else:
            print(answer)


def problem(rows, cols, board):
    VOID, WALL, REACH, FIRE = 46, 35, 64, 42
    DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    fires = []
    reaches = []
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem == FIRE:
                fires.append((i, j))
            if elem == REACH:
                reaches.append((i, j))

    time = 0
    while True:
        time += 1

        next_fires = []
        for y, x in fires:
            for dy, dx in DELTAS:
                if 0 <= (ny := y + dy) < rows and 0 <= (nx := x + dx) < cols and board[ny][nx] == VOID:
                    next_fires.append((ny, nx))
                    board[ny][nx] = FIRE
        fires = next_fires

        next_reaches = []
        for y, x in reaches:
            for dy, dx in DELTAS:
                if 0 <= (ny := y + dy) < rows and 0 <= (nx := x + dx) < cols:
                    if board[ny][nx] == VOID:
                        next_reaches.append((ny, nx))
                        board[ny][nx] = REACH
                else:
                    return time
        reaches = next_reaches

        if not reaches:
            return -1


if __name__ == "__main__":
    sys.exit(main())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20210805|162292|312|PyPy3|1603
#### **📝해설**

```python
from collections import deque

T = int(input())

def find_start():
    # 시작 지점을 찾는 함수
    for i in range(N):
        for j in range(M):
            if table[i][j] == '@':
                table[i][j] = '.'
                return (i, j)

for testcase in range(T):
    # 입력받기
    M, N = map(int, input().split())
    table = [list(input()) for _ in range(N)]

    # 방문 여부를 처리할 리스트
    visited = [[False] * M for _ in range(N)]

    # 현재 상근이가 있을 수 있는 좌표들을 담은 deque(큐)
    now_q = deque()
    # 시작 위치를 저장
    start = find_start()
    # 시작 위치 방문 처리
    visited[start[0]][start[1]] = True
    # 시작 위치를 삽입후 시작
    now_q.append(start)

    # 탈출여부, 불가능 여부를 변수에 저장
    escape = False
    impossible = False

    # 상하좌우 탐색을 위한 리스트
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 몇초가 지났는지 저장할 변수
    count = 0

    # 현재 불의 위치를 저장할 리스트
    now_fire = []
    # 현재 불의 위치를 리스트에 저장
    for i in range(N):
        for j in range(M):
            if table[i][j] == '*':
                now_fire.append((i, j))

    # 탈출했거나, 탈출 못하는 경우 반복 종료
    while not escape and not impossible:

        # 옮겨진 불의 위치를 저장할 리스트
        next_fire = []
        
        # 불을 모두 옮겨주고, 다음 불의 위치를 저장
        for fire in now_fire:
            for i in range(4):
                nx = fire[0] + dx[i]
                ny = fire[1] + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if table[nx][ny] == '.':
                        table[nx][ny] = '*'
                        next_fire.append((nx, ny))
        
        now_fire = next_fire

        # 다음 상근이가 있을 수 있는 위치를 저장할 deque
        next_queue = deque()

        # 현재 상근이가 있을 수 있는 위치를 BFS로 순회하면서 다음 위치로 삽입
        while now_q:
            now = now_q.popleft()

            for i in range(4):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]

                # 만약 인덱스를 벗어나지 않는다면
                if 0 <= nx < N and 0 <= ny < M:
                    # 아직 방문하지 않았고 빈공간이라면
                    if not visited[nx][ny] and table[nx][ny] == '.':
                        # 다음 상근이의 위치 큐에 삽입
                        next_queue.append((nx, ny))
                        # 방문처리
                        visited[nx][ny] = True
                # 인덱스를 벗어났다면 == 상근이가 탈출했다면
                else:
                    # 탈출을 True로 바꿈
                    escape = True

        # 이동할 수 있는 위치가 없다면 impossible을 true로 바꿈
        if next_queue == deque():
            impossible = True
        else:
            # 이동할 수 있는 위치가 있다면 새롭게 now_q를 갱신
            now_q = next_queue

        # 시간을 더해줌
        count += 1
        
    # 탈출 가능하다면 시간출력, 아니라면 IMPOSSIBLE
    if escape == True:
        print(count)
    else:
        print('IMPOSSIBLE')
```

### **🔖정리**

1. 배운점