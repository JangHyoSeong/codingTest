# [13565] 침투

### **난이도**
실버 2
## **📝문제**
인제대학교 생화학연구실에 재직중인 석교수는 전류가 침투(percolate) 할 수 있는 섬유 물질을 개발하고 있다. 이 섬유 물질은 2차원 M × N 격자로 표현될 수 있다. 편의상 2차원 격자의 위쪽을 바깥쪽(outer side), 아래쪽을 안쪽(inner side)라고 생각하기로 한다. 또한 각 격자는 검은색 아니면 흰색인데, 검은색은 전류를 차단하는 물질임을 뜻하고 흰색은 전류가 통할 수 있는 물질임을 뜻한다. 전류는 섬유 물질의 가장 바깥쪽 흰색 격자들에 공급되고, 이후에는 상하좌우로 인접한 흰색 격자들로 전달될 수 있다.

김 교수가 개발한 섬유 물질을 나타내는 정보가 2차원 격자 형태로 주어질 때, 바깥쪽에서 흘려 준 전류가 안쪽까지 침투될 수 있는지 아닌지를 판단하는 프로그램을 작성하시오.

	
(a) The current percolates.	(b) The current does not percolate.
예를 들어, Figure 1(a) 에서는 바깥쪽에서 공급된 전류가 안쪽까지 침투하지만, Figure 1(b)에서는 그렇지 못한다.
### **입력**
첫째 줄에는 격자의 크기를 나타내는  M (2 ≤ M ≤ 1,000) 과 N (2 ≤ N ≤ 1,000) 이 주어진다. M줄에 걸쳐서, N개의 0 또는 1 이 공백 없이 주어진다. 0은 전류가 잘 통하는 흰색, 1은 전류가 통하지 않는 검은색 격자임을 뜻한다.
### **출력**
바깥에서 흘려준 전류가 안쪽까지 잘 전달되면 YES를 출력한다.

그렇지 않으면 NO를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 6
010101
010000
011101
100011
001011
```

**예제 출력1**

```
NO
```

**예제 입력2**

```
8 8
11000111
01100000
00011001
11001000
10001001
10111100
01010000
00001011
```

**예제 출력2**

```
YES
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
M, N = map(int, input().split())
table = [list(input()) for _ in range(M)]

visited = [[False] * N for _ in range(M)]

stack = []
for i in range(N):
    if table[0][i] == '0':
        stack.append([0, i])
        visited[0][i] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while stack:
    x, y = stack.pop()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and table[nx][ny] == '0':
            if nx == M-1:
                print('YES')
                exit()
            visited[nx][ny] = True
            stack.append([nx, ny])

print('NO')

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|67688|544|Python3|631
#### **📝해설**

**알고리즘**
```
1. DFS
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def graph(i, j):
    visited[i][j] = 1

    if(i == M - 1):
        print("YES")
        exit()

    if (i+1 < M):
        if (_map[i+1][j] == '0' and visited[i+1][j] != 1):
            graph(i+1, j)
    
    if (i-1 >= 0):
        if (_map[i-1][j] == '0' and visited[i-1][j] != 1):
            graph(i-1, j)
    
    if (j+1 < N):
        if (_map[i][j+1] == '0' and visited[i][j+1] != 1):
            graph(i, j+1)
    
    if (j-1 >= 0):
        if(_map[i][j-1] == '0' and visited[i][j-1] != 1):
            graph(i, j-1)


M, N = map(int, input().split())

_map = list()
visited = [[0] * N for _ in range(M)]

for i in range(M):
    _map.append(list(input()))

for j in range(N):
    if(_map[0][j] == "0"):
        graph(0, j)

print("NO")
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
woojin8787|43960|104|Python3|811
#### **📝해설**

```python
# 입력
M, N = map(int, input().split())
table = [list(input()) for _ in range(M)]

# 방문 여부 저장
visited = [[False] * N for _ in range(M)]

# DFS에 사용할 스택 선언
stack = []

# 초기 정보 삽입
for i in range(N):
    if table[0][i] == '0':
        stack.append([0, i])
        visited[0][i] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# DFS
while stack:
    x, y = stack.pop()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and table[nx][ny] == '0':
            if nx == M-1:
                print('YES')
                exit()
            visited[nx][ny] = True
            stack.append([nx, ny])

print('NO')

```