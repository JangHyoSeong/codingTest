# [2583] 영역 구하기

### **난이도**
실버 1
## **📝문제**
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.

![이미지](https://www.acmicpc.net/upload/images/zzJD2aQyF5Rm4IlOt.png)

<그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.

M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.
### **출력**
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.
### **예제입출력**

**예제 입력1**

```
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
```

**예제 출력1**

```
3
1 7 13
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from pprint import pprint

M, N, K = map(int, input().split())

table = [[False] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            table[y][x] = True

count = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
area = []
for i in range(M):
    for j in range(N):
        if table[i][j]:
            continue

        count += 1
        stack = [(i, j)]
        table[i][j] = True
        size = 1
        while stack:
            x, y = stack.pop()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < M and 0 <= ny < N and not table[nx][ny]:
                    stack.append((nx, ny))
                    size += 1
                    table[nx][ny] = True
        
        area.append(size)

print(count)
print(" ".join(map(str, sorted(area))))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|42140|220|Python3|899
#### **📝해설**

**알고리즘**
```
1. 격자 그래프
```

### **다른 풀이**

```python
'''

'''

import sys
input = sys.stdin.readline
M,N,K = map(int,input().split())

chk = [[0]*N for _ in range(M)]

for _ in range(K):
    x_1,y_1,x_2,y_2 = map(int,input().split())
    for i in range(x_1,x_2):
        for j in range(y_1,y_2):
            chk[j][i] = 1

def bfs(y,x):
    q = [(y,x)]
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    rs = 1
    chk[y][x] = 1
    while q:
        y,x = q.pop()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<M and 0<=nx<N and chk[ny][nx]==0 :
                q.append((ny,nx))
                chk[ny][nx]=1
                rs +=1

    return rs
tmp = []
for i in range(M):
    for j in range(N):
        if chk[i][j]==0:
            tmp.append(bfs(i,j))

print(len(tmp))
print(' '.join(map(str,sorted(tmp))))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ko5737|31120|36|Python3|788
#### **📝해설**

```python
from pprint import pprint

M, N, K = map(int, input().split())

# 직사각형이 포함되어있는지 여부
table = [[False] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            table[y][x] = True

count = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
area = []

# 모든 구간을 탐색하면서
for i in range(M):
    for j in range(N):

        # 빈 곳이 아니라면 건너뜀
        if table[i][j]:
            continue

        # 빈곳이라면, 구역 갯수 ++
        count += 1

        # 현재 위치부터 DFS로 영역의 넓이를 구함
        stack = [(i, j)]
        table[i][j] = True
        size = 1
        while stack:
            x, y = stack.pop()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < M and 0 <= ny < N and not table[nx][ny]:
                    stack.append((nx, ny))
                    size += 1
                    table[nx][ny] = True
        
        area.append(size)

# 출력
print(count)
print(" ".join(map(str, sorted(area))))
```