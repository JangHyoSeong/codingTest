# [2468] 안전영역

### **난이도**
실버 1
## **📝문제**
재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다. 먼저 어떤 지역의 높이 정보를 파악한다. 그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다. 이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.

어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다. 예를 들어, 다음은 N=5인 지역의 높이 정보이다.

6	8	2	6	2
3	2	3	4	6
6	7	3	3	2
7	2	5	3	6
8	9	5	2	7
이제 위와 같은 지역에 많은 비가 내려서 높이가 4 이하인 모든 지점이 물에 잠겼다고 하자. 이 경우에 물에 잠기는 지점을 회색으로 표시하면 다음과 같다.

6	8	2	6	2
3	2	3	4	6
6	7	3	3	2
7	2	5	3	6
8	9	5	2	7
물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다. 위의 경우에서 물에 잠기지 않는 안전한 영역은 5개가 된다(꼭짓점으로만 붙어 있는 두 지점은 인접하지 않는다고 취급한다).

또한 위와 같은 지역에서 높이가 6이하인 지점을 모두 잠기게 만드는 많은 비가 내리면 물에 잠기지 않는 안전한 영역은 아래 그림에서와 같이 네 개가 됨을 확인할 수 있다.

6	8	2	6	2
3	2	3	4	6
6	7	3	3	2
7	2	5	3	6
8	9	5	2	7
이와 같이 장마철에 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다. 위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.

어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.
### **출력**
첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
```

**예제 출력1**

```
5
```

**예제 입력2**

```
7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9
```

**예제 출력2**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# 최대 영역 개수. 최소값은 1
max_area = 1

# 상하좌우 탐색을 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 모든 높이에 대해 영역의 개수를 검사
for height in range(1, 100):

    # 이번 높이에서 영역의 개수
    temp_area = 0

    # 방문 여부를 저장할 리스트
    visited = [[False] * N for _ in range(N)]

    # 이중리스트를 모두 순회하면서
    for i in range(N):
        for j in range(N):

            # 이미 방문한 곳이거나, 물에 잠긴곳이라면 다음 위치로 이동
            if visited[i][j] or table[i][j] <= height:
                # 최적화를 위해 방문처리를 해줌
                visited[i][j] = True
                continue
            

            # 이미 방문하지 않고, 비에 잠기지 않은 곳이라면
            else:

                # 방문처리, 영역의 개수를 증가
                visited[i][j] = True
                temp_area += 1
                
                # DFS를 위한 스택 선언
                stack = [(i, j)]

                # DFS
                while stack:    
                    x, y = stack.pop()

                    # 상하좌우를 탐색
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]

                        # 이동할수있는 위치라면 방문
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and table[nx][ny] > height:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
    max_area = max(max_area, temp_area)

print(max_area)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|112796|236|PyPy3|942
#### **📝해설**

**알고리즘**
```
1. DFS
```

### **다른 풀이**

```python
import sys
from collections import defaultdict

N = int(sys.stdin.readline())
d = defaultdict(list)

for i, row in enumerate(sys.stdin.readlines()):
    for j, v in enumerate(row.split()):
        d[v].append((i, j))

parents = [[0]*N for _ in range(N)]

def get_root(coor):
    p = parents[coor[0]][coor[1]]
    temp = []
    while p != coor:
        temp.append(coor)
        p, coor = parents[p[0]][p[1]], p
    for i, j in temp:
        parents[i][j] = p
    return p

answer = 1
n = 0

for v in sorted(map(int, d), reverse=True)[:-1]:
    for i, j in d[str(v)]:
        connected = set()
        for i_, j_ in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if 0 <= i_ < N and 0 <= j_ < N and parents[i_][j_] != 0:
                connected.add(get_root((i_, j_)))
        if len(connected) == 0:
            n += 1
            parents[i][j] = (i, j)
        elif len(connected) == 1:
            parents[i][j] = connected.pop()
        else:
            root = connected.pop()
            n -= len(connected)
            parents[i][j] = root
            for coor in connected:
                parents[coor[0]][coor[1]] = root

    if answer < n:
        answer = n

print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
legendre13|34208|88|Python3|1191