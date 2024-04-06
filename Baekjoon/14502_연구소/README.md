# [14502] 연구소

### **난이도**
골드 4
## **📝문제**
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0  
0 0 1 0 1 2 0  
0 1 1 0 1 0 0  
0 1 0 0 0 0 0  
0 0 0 0 0 1 1  
0 1 0 0 0 0 0  
0 1 0 0 0 0 0  
이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0  
1 0 1 0 1 2 0  
0 1 1 0 1 0 0  
0 1 0 0 0 1 0  
0 0 0 0 0 1 1  
0 1 0 0 0 0 0  
0 1 0 0 0 0 0  
바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2  
1 0 1 0 1 2 2  
0 1 1 0 1 2 2  
0 1 0 0 0 1 2  
0 0 0 0 0 1 1  
0 1 0 0 0 0 0  
0 1 0 0 0 0 0  
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.
### **출력**
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
### **예제입출력**

**예제 입력1**

```
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
```

**예제 출력1**

```
27
```

**예제 입력2**

```
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
```

**예제 출력2**

```
9
```

**예제 입력3**

```
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```

**예제 출력3**

```
3
```
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

max_safe = 0

zero_list = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zero_list.append((i, j))
        elif lab[i][j] ==2:
            virus.append((i, j))

barricade = list(combinations(zero_list, 3))

for case in barricade:
    temp_lab = deepcopy(lab)

    for x, y in case:
        temp_lab[x][y] = 1
    
    q = deque(virus)
    temp_safe = 0
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                q.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 0:
                temp_safe += 1

    max_safe = max(temp_safe, max_safe)

print(max_safe)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|119920|632|PyPy3|1069
#### **📝해설**

**알고리즘**
```
1. BFS
2. 완전탐색
```
### **다른 풀이**

```python
from sys import stdin
from itertools import combinations
input = stdin.readline
def solve():
    blanks = []
    virus = []
    for i in range(length):
        if world[i] == 0:
            blanks.append(i)
        elif world[i] == 2:
            virus.append(i)

    not_wall = len(blanks) + len(virus) - 3
    ans = 0 
    
    for build in combinations(blanks, 3):
        q = virus[:]
        tmp_world = world[:]
        infection = 0
        
        for pos in build:
            tmp_world[pos] = 1
            
        while q:
            idx = q.pop()
            infection += 1
            r, c = idx // M, idx % M
            adj = [
                idx - M if 0 < r else -1, #첫 줄이 아니면 상
                idx + M if r < N - 1 else -1, #마지막 줄이 아니면 하
                idx - 1 if 0 < c else -1, #첫번째가 아니면 좌
                idx + 1 if c < M - 1 else -1 # 마지막이 아니면 우
            ]
            
            for nxt in adj:
                if nxt != -1 and tmp_world[nxt] == 0:
                    tmp_world[nxt] = 2
                    q.append(nxt)

        cur = not_wall - infection
        if ans < cur:
            ans = cur

    return ans


if __name__ == '__main__':
    N, M = map(int, input().split())
    length = N * M
    world = [0] * length
    
    for i in range(0, length, M): # 1차원 배열
        world[i:i + M] = [*map(int, input().split())]
        
    print(solve())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rhzn5512|115368|248|PyPy3|1461
#### **📝해설**

```python
from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 델타 탐색을 위한 리스트 선언
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 결과값으로 사용할 max_safe
max_safe = 0


zero_list = [] # 초기 상태에서 빈공간의 위치를 저장할 리스트
virus = [] # 초기 상태에서 바이러스의 위치를 저장할 리스트

# 바이러스와 빈공간을 탐색하면서 저장해둠
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zero_list.append((i, j))
        elif lab[i][j] ==2:
            virus.append((i, j))

# 0의 위치를 3개씩 묶어서 조합을 만들어줌
# 벽을 세울 위치를 가지게 됨
barricade = list(combinations(zero_list, 3))

# 모든 케이스를 검사
for case in barricade:
    # 깊은 복사로 연구실의 리스트를 복사함
    temp_lab = deepcopy(lab)

    # 이번 케이스에서 벽을 세워줌ㅈ
    for x, y in case:
        temp_lab[x][y] = 1
    
    # BFS를 위한 deque 선언, 초기값을 넣어줌
    q = deque(virus)
    # 이번 케이스에서의 안전 구역
    temp_safe = 0
    
    # BFS시작
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인덱스를 벗어나지않고, 빈공간이라면 바이러스로 바꾸어주고, q에 삽입
            if 0 <= nx < N and 0 <= ny < M and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                q.append((nx, ny))

    # 연구소를 순회하면서 빈공간 개수를 세어줌
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 0:
                temp_safe += 1

    # max값을 갱신
    max_safe = max(temp_safe, max_safe)

print(max_safe)
```