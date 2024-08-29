# [1987] 알파벳

### **난이도**
골드 4
## **📝문제**
세로 $R$칸, 가로 $C$칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 ($1$행 $1$열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.
### **입력**
첫째 줄에 $R$과 $C$가 빈칸을 사이에 두고 주어진다. $(1 ≤ R,C ≤ 20)$둘째 줄부터 $R$개의 줄에 걸쳐서 보드에 적혀 있는 $C$개의 대문자 알파벳들이 빈칸 없이 주어진다.
### **출력**
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.


### **예제입출력**

**예제 입력1**

```
2 4
CAAB
ADCB
```

**예제 출력1**

```
3
```

**예제 입력2**

```
3 6
HFDFFB
AJHGDH
DGAGEH
```

**예제 출력2**

```
6
```

**예제 입력3**

```
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
```

**예제 출력3**

```
10
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def dfs(x, y, count, visited):
    
    global max_count

    if max_count < count:
        max_count = count

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and table[nx][ny] not in visited:
            visited.add(table[nx][ny])
            dfs(nx, ny, count+1, visited)
            visited.remove(table[nx][ny])


R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_count = 0

dfs(0, 0, 1, set(table[0][0]))

print(max_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|171268|7280|PyPy3|557
#### **📝해설**

**알고리즘**
```
1. DFS
2. 백트래킹
```

#### **😅개선점**

1. 처음에 단순히 BFS로 풀다가 메모리 초과가 났다. 하나의 케이스에 대해 모두 visited 딕셔너리를 두었기 때문. 백트래킹을 통해 계산해야 메모리 초과가 나지 않는다.

### **다른 풀이**

```python
from sys import stdin
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
r, c = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
visited = [[0]*c for _ in range(r)]
_max = (1 << 26) - 1
ans = 1
stack = [(1, 0, 0, 1 << (ord(grid[0][0]) - 65))]
while stack:
    depth, i, j, path = stack.pop()
    if depth > ans:
        ans = depth
        if path == _max:
            print(ans)
            exit()
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0<=ni<r and 0<=nj<c:
            letter = 1 << (ord(grid[ni][nj]) - 65)
            if not (path & letter) and visited[ni][nj] != (path|letter):
                visited[ni][nj] = path|letter
                stack.append((depth + 1, ni, nj, path|letter))
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
line1029|115092|152|PyPy3|735
#### **📝해설**

```python
def dfs(x, y, count, visited):
    # bfs 함수    
    global max_count

    # 최대값이 갱신이 가능하다면 갱신
    if max_count < count:
        max_count = count

    # 상하좌우 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스를 벗어나지않고 아직 가지 않은 알파벳이라면 이동
        if 0 <= nx < R and 0 <= ny < C and table[nx][ny] not in visited:
            # 방문처리
            visited.add(table[nx][ny])
            # 이동
            dfs(nx, ny, count+1, visited)
            # bfs를 벗어나면 방문처리 제거(백트래킹)
            visited.remove(table[nx][ny])


R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_count = 0

dfs(0, 0, 1, set(table[0][0]))

print(max_count)
```

### **🔖정리**

1. 백트래킹이 가능한지 여부를 잘 판단하자