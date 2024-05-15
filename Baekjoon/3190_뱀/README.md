# [3190] 뱀

### **난이도**
골드 4
## **📝문제**
'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

- 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
- 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
- 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
- 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.  
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
### **입력**
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.
### **출력**
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.
### **예제입출력**

**예제 입력1**

```
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
```

**예제 출력1**

```
9
```

**예제 입력2**

```
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
```

**예제 출력2**

```
21
```

**예제 입력3**

```
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
```

**예제 출력3**

```
13
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input())

swap = {}
for _ in range(L):
    temp = list(input().split())
    swap[int(temp[0])] = temp[1]

q = deque([(1, 1)])

time = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0
flag = True

while True:

    head = q.popleft()
    new_head = (head[0] + dx[direction], head[1] + dy[direction])
    
    if new_head[0] < 1 or new_head[0] > N or new_head[1] < 1 or new_head[1] > N:
        break

    for i in range(len(q)):
        if new_head == q[i]:
            flag = False
            break
    
    if flag == False:
        break

    for i in range(K):
        if new_head[0] == apples[i][0] and new_head[1] == apples[i][1]:
            apples[i] = [-1, -1]
            q.appendleft(head)
            q.appendleft(new_head)
            break
    else:
        q.appendleft(head)
        q.appendleft(new_head)
        q.pop()

    if swap.get(time) is not None:
        if swap[time] == 'L':
            direction = (direction-1) % 4
        else:
            direction = (direction+1) % 4
    time += 1

print(time)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|113944|164|PyPy3|1169
#### **📝해설**

**알고리즘**
```
1. 덱
```

#### **📝해설**

```python
from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input())

# 방향전환은 딕셔너리로 입력받음
# 키 값은 방향전환 시간
# value값은 방향전환 방향
swap = {}
for _ in range(L):
    temp = list(input().split())
    swap[int(temp[0])] = temp[1]

# 시작 위치를 덱에 넣고 시작
q = deque([(1, 1)])

# 1초부터 시작
time = 1

# 방향전환을 위한 리스트. 순서대로 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 현재 방향. 오른쪽부터 시작
direction = 0

# 벽에 부딪히거나 자신을 만나면 False로 바뀌어 반복 종료
flag = True

while True:

    # head를 pop
    # 덱에 왼쪽(인덱스 0)은 머리, 오른쪽(인덱스 마지막)은 꼬리가 됨
    head = q.popleft()

    # 새 머리를 만들어 줌
    new_head = (head[0] + dx[direction], head[1] + dy[direction])
    
    # 벽에 부딪히면 반복 종료
    if new_head[0] < 1 or new_head[0] > N or new_head[1] < 1 or new_head[1] > N:
        break

    # 자신의 몸을 순회해서 부딪히는지 검사. 부딪히면 종료
    for i in range(len(q)):
        if new_head == q[i]:
            flag = False
            break
    
    if flag == False:
        break

    # 사과 리스트를 순회하여, 현재 새로운 머리 위치가 사과위치라면 사과를 먹음
    for i in range(K):
        if new_head[0] == apples[i][0] and new_head[1] == apples[i][1]:
            # 먹은 사과는 먹을수 없도록 위치 초기화
            apples[i] = [-1, -1]
            q.appendleft(head)
            q.appendleft(new_head)
            break
    # 사과를 먹지 못했다면 꼬리의 맨 뒤를 지워줌
    else:
        q.appendleft(head)
        q.appendleft(new_head)
        q.pop()

    # 방향전환
    # 방향전환은 먹고 난 뒤 해줘야함 <- 문제에서 제대로 안적어줘서 좀 헤맸다
    if swap.get(time) is not None:
        if swap[time] == 'L':
            direction = (direction-1) % 4
        else:
            direction = (direction+1) % 4
    time += 1

print(time)
```