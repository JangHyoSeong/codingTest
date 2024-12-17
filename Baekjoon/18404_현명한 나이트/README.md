# [18404] 현명한 나이트

### **난이도**
실버 1
## **📝문제**
NxN 크기 체스판의 특정한 위치에 하나의 나이트가 존재한다. 이때 M개의 상대편 말들의 위치 값이 주어졌을 때, 각 상대편 말을 잡기 위한 나이트의 최소 이동 수를 계산하는 프로그램을 작성하시오.
나이트는 일반적인 체스(Chess)에서와 동일하게 이동할 수 있다. 현재 나이트의 위치를 (X,Y)라고 할 때, 나이트는 다음의 8가지의 위치 중에서 하나의 위치로 이동한다.

(X-2,Y-1), (X-2,Y+1), (X-1,Y-2), (X-1,Y+2), (X+1,Y-2), (X+1,Y+2), (X+2,Y-1), (X+2,Y+1)

N=5일 때, 나이트가 (3,3)의 위치에 존재한다면 이동 가능한 위치는 다음과 같다. 나이트가 존재하는 위치는 K, 이동 가능한 위치는 노란색으로 표현하였다.



예를 들어 N=5, M=3이고, 나이트가 (2,4)의 위치에 존재한다고 가정하자. 또한 상대편 말의 위치가 차례대로 (3,2), (3,5), (4,5)라고 하자. 이때 각 상대편 말을 잡기 위한 최소 이동 수를 계산해보자. 아래 그림에서는 상대편 말의 위치를 E로 표현하였다. 단, 본 문제에서 위치 값을 나타낼 때는 (행,열)의 형태로 표현한다.



각 상대편 말을 잡기 위한 최소 이동 수는 차례대로 1, 2, 1이 된다.
### **입력**
첫째 줄에 N과 M이 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ N ≤ 500, 1 ≤ M ≤ 1,000) 둘째 줄에 나이트의 위치 (X, Y)를 의미하는 X와 Y가 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ X, Y ≤ N) 셋째 줄부터 M개의 줄에 걸쳐 각 상대편 말의 위치 (A, B)를 의미하는 A와 B가 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ A, B ≤ N)

단, 입력으로 주어지는 모든 말들의 위치는 중복되지 않으며, 나이트가 도달할 수 있는 위치로만 주어진다.
### **출력**
첫째 줄에 각 상대편 말을 잡기 위한 최소 이동 수를 공백을 기준으로 구분하여 출력한다.

단, 출력할 때는 입력 시에 상대편 말 정보가 주어졌던 순서에 맞게 차례대로 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
2 4
3 2
3 5
4 5
```

**예제 출력1**

```
1 2 1
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())
X, Y = map(int, input().split())
targets = [list(map(int, input().split())) for _ in range(M)]

move_table = [[21e8] * N for _ in range(N)]
move_table[X-1][Y-1] = 0

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

q = deque([(X-1, Y-1)])
while q:
    x, y = q.popleft()

    for move in moves:
        nx, ny = x + move[0], y + move[1]
        if 0 <= nx < N and 0 <= ny < N and move_table[nx][ny] > move_table[x][y] + 1:
            move_table[nx][ny] = move_table[x][y] + 1
            q.append((nx, ny))

for target in targets:
    print(move_table[target[0]-1][target[1]-1], end=" ")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|119140|196|PyPy3|686
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

# 입력받기
N, M = map(int, input().split())
X, Y = map(int, input().split())
targets = [list(map(int, input().split())) for _ in range(M)]

# 이동횟수를 저장할 테이블
move_table = [[21e8] * N for _ in range(N)]

# 시작위치는 0으로 초기화
move_table[X-1][Y-1] = 0

# 나이트의 움직임을 나타내는 리스트
moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# BFS를 위한 queue 선언
q = deque([(X-1, Y-1)])

# BFS
while q:
    x, y = q.popleft()

    # 다음 위치를 검사
    for move in moves:

        # 새 좌표
        nx, ny = x + move[0], y + move[1]

        # 인덱스를 벗어나지 않고, 이동횟수가 갱신이 가능하다면
        if 0 <= nx < N and 0 <= ny < N and move_table[nx][ny] > move_table[x][y] + 1:

            # 그 위치로이동
            move_table[nx][ny] = move_table[x][y] + 1
            q.append((nx, ny))

# 목표한 위치의 이동횟수를 출력
for target in targets:
    print(move_table[target[0]-1][target[1]-1], end=" ")

```