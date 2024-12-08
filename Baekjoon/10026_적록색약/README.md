# [10026] 적록색약

### **난이도**
골드 5
## **📝문제**
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

```
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
```
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.
### **출력**
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
### **예제입출력**

**예제 입력1**

```
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
```

**예제 출력1**

```
4 3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
table = [list(input()) for _ in range(N)]

def dfs(x, y, visited, grid, color):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                stack.append((nx, ny))

def count_regions(grid):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, visited, grid, grid[i][j])
                count += 1
    return count

normal_count = count_regions(table)
for i in range(N):
    for j in range(N):
        if table[i][j] in 'RG':
            table[i][j] = 'R'
colorblind_count = count_regions(table)

print(normal_count, colorblind_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|48|Python3|944
#### **📝해설**

**알고리즘**
```
1. DFS
```

#### **📝해설**

```python
N = int(input())
table = [list(input()) for _ in range(N)]

# DFS를 하는 함수
def dfs(x, y, visited, grid, color):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                stack.append((nx, ny))

# 몇개의 구역으로 나누어져 있는지 검사하는 함수
def count_regions(grid):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, visited, grid, grid[i][j])
                count += 1
    return count

# 일반적인 상황에서의 구역 검출
normal_count = count_regions(table)

# 적록색약인 사람에게 보이는 그림을 새로 작성
for i in range(N):
    for j in range(N):
        if table[i][j] in 'RG':
            table[i][j] = 'R'

# 적록색약인 경우 몇 구역인지 검출
colorblind_count = count_regions(table)

# 출력
print(normal_count, colorblind_count)
```

### **🔖정리**

1. 코드의 중복을 줄이기 위해 함수로 작성하자