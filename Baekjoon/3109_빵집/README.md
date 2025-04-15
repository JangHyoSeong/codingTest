# [3109] 빵집

### **난이도**
골드 2
## **📝문제**
유명한 제빵사 김원웅은 빵집을 운영하고 있다. 원웅이의 빵집은 글로벌 재정 위기를 피해가지 못했고, 결국 심각한 재정 위기에 빠졌다.

원웅이는 지출을 줄이고자 여기저기 지출을 살펴보던 중에, 가스비가 제일 크다는 것을 알게되었다. 따라서 원웅이는 근처 빵집의 가스관에 몰래 파이프를 설치해 훔쳐서 사용하기로 했다.

빵집이 있는 곳은 R*C 격자로 표현할 수 있다. 첫째 열은 근처 빵집의 가스관이고, 마지막 열은 원웅이의 빵집이다.

원웅이는 가스관과 빵집을 연결하는 파이프를 설치하려고 한다. 빵집과 가스관 사이에는 건물이 있을 수도 있다. 건물이 있는 경우에는 파이프를 놓을 수 없다.

가스관과 빵집을 연결하는 모든 파이프라인은 첫째 열에서 시작해야 하고, 마지막 열에서 끝나야 한다. 각 칸은 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결할 수 있고, 각 칸의 중심끼리 연결하는 것이다.

원웅이는 가스를 되도록 많이 훔치려고 한다. 따라서, 가스관과 빵집을 연결하는 파이프라인을 여러 개 설치할 것이다. 이 경로는 겹칠 수 없고, 서로 접할 수도 없다. 즉, 각 칸을 지나는 파이프는 하나이어야 한다.

원웅이 빵집의 모습이 주어졌을 때, 원웅이가 설치할 수 있는 가스관과 빵집을 연결하는 파이프라인의 최대 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 R과 C가 주어진다. (1 ≤ R ≤ 10,000, 5 ≤ C ≤ 500)

다음 R개 줄에는 빵집 근처의 모습이 주어진다. '.'는 빈 칸이고, 'x'는 건물이다. 처음과 마지막 열은 항상 비어있다.
### **출력**
첫째 줄에 원웅이가 놓을 수 있는 파이프라인의 최대 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 5
.xx..
..x..
.....
...x.
...x.
```

**예제 출력1**

```
2
```

**예제 입력2**

```
6 10
..x.......
.....x....
.x....x...
...x...xx.
..........
....x.....
```

**예제 출력2**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
sys.setrecursionlimit(100000)

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(x, y):
    if y == C - 1:
        return True

    for dir in range(3):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True
    return False

answer = 0
for i in range(R):
    if dfs(i, 0):
        answer += 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|503000|1484|PyPy3|661
#### **📝해설**

**알고리즘**
```
1. DFS
2. 그리디 알고리즘
```

### **다른 풀이**

```python
import io, os, sys


def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    rows, cols = map(int, input().split())
    grid = [list(input()) for _ in range(rows)]
    # '.' = 46, 'x' = 120

    answer = 0
    path = []
    for i in range(rows):
        path.clear()
        path.append(i)
        while len(path) - 1 < cols:
            i = path[-1]
            for di in (-1, 0, 1):
                ni = i + di
                if 0 <= ni < rows and grid[ni][len(path) - 1] == 46:
                    grid[ni][len(path) - 1] = 0
                    path.append(ni)
                    break
            else:
                path.pop()
                if not path:
                    break
        else:
            answer += 1
    print(answer)


if __name__ == "__main__":
    sys.exit(main())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20210805|156032|404|PyPy3|824
#### **📝해설**

```python
import sys
sys.setrecursionlimit(100000)

# 입력
R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

# 오른쪽 위, 오른쪽, 오른쪽 아래 방향
# 항상 오른쪽 위, 중간, 아래 순서로 탐색하면 최선의 경우로 탐색이 가능
dx = [-1, 0, 1]
dy = [1, 1, 1]

# DFS 재귀함수
def dfs(x, y):

    # 끝 열에 닿으면 종료
    if y == C - 1:
        return True

    # 움직일 수 있는 방향으로 움직임
    for dir in range(3):
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 인덱스를 벗어나지 않고
        if 0 <= nx < R and 0 <= ny < C:
            # 이동할 수 있는 위치라면
            if board[nx][ny] == '.' and not visited[nx][ny]:
                # 방문처리
                visited[nx][ny] = True

                # 다음 노드로 이동
                if dfs(nx, ny):
                    return True
                    
    # 더이상 이동이 불가능하면 False 반환
    return False

# 모든 시작점에서부터 검사
answer = 0
for i in range(R):
    if dfs(i, 0):
        answer += 1

print(answer)
```