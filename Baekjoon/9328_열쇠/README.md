# [9328] 열쇠

### **난이도**
골드 1
## **📝문제**
상근이는 1층 빌딩에 침입해 매우 중요한 문서를 훔쳐오려고 한다. 상근이가 가지고 있는 평면도에는 문서의 위치가 모두 나타나 있다. 빌딩의 문은 모두 잠겨있기 때문에, 문을 열려면 열쇠가 필요하다. 상근이는 일부 열쇠를 이미 가지고 있고, 일부 열쇠는 빌딩의 바닥에 놓여져 있다. 상근이는 상하좌우로만 이동할 수 있다.

상근이가 훔칠 수 있는 문서의 최대 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 수는 100개를 넘지 않는다.

각 테스트 케이스의 첫째 줄에는 지도의 높이와 너비 h와 w (2 ≤ h, w ≤ 100)가 주어진다. 다음 h개 줄에는 빌딩을 나타내는 w개의 문자가 주어지며, 각 문자는 다음 중 하나이다.

- '.'는 빈 공간을 나타낸다.
- '*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없다.
- '$'는 상근이가 훔쳐야하는 문서이다.
- 알파벳 대문자는 문을 나타낸다.
- 알파벳 소문자는 열쇠를 나타내며, 그 문자의 대문자인 모든 문을 열 수 있다.

마지막 줄에는 상근이가 이미 가지고 있는 열쇠가 공백없이 주어진다. 만약, 열쇠를 하나도 가지고 있지 않는 경우에는 "0"이 주어진다.

상근이는 처음에는 빌딩의 밖에 있으며, 빌딩 가장자리의 벽이 아닌 곳을 통해 빌딩 안팎을 드나들 수 있다. 각각의 문에 대해서, 그 문을 열 수 있는 열쇠의 개수는 0개, 1개, 또는 그 이상이고, 각각의 열쇠에 대해서, 그 열쇠로 열 수 있는 문의 개수도 0개, 1개, 또는 그 이상이다. 열쇠는 여러 번 사용할 수 있다.
### **출력**
각 테스트 케이스 마다, 상근이가 훔칠 수 있는 문서의 최대 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony
```

**예제 출력1**
```
3
1
0
```

**예제 입력2**

```
```

**예제 출력2**

```
```

**예제 입력3**

```
```

**예제 출력3**

```
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

T = int(input())

for testcase in range(T):
    h, w = map(int, input().split())
    table = [list(input()) for _ in range(h)]

    h += 2
    w += 2

    new_table = [['.'] * w for _ in range(h)]
    for i in range(1, h-1):
        for j in range(1, w-1):
            new_table[i][j] = table[i-1][j-1]
    

    keys = set(input())
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False] * w for _ in range(h)]
    q = deque([(0, 0)])
    visited[0][0] = True

    doors = {chr(c): [] for c in range(ord('A'), ord('Z') + 1)}

    count = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                cell = new_table[nx][ny]

                if cell == '*':
                    continue

                visited[nx][ny] = True

                if cell == '.':
                    q.append((nx, ny))
                
                elif cell == '$':
                    q.append((nx, ny))
                    count += 1

                elif 'a' <= cell <= 'z':
                    if cell not in keys:
                        keys.add(cell)
                        door_char = cell.upper()
                        while doors[door_char]:
                            q.append((doors[door_char].pop()))
                    
                    q.append((nx, ny))
                
                elif 'A' <= cell <= 'Z':
                    if cell.lower() in keys:
                        q.append((nx, ny))
                    else:
                        doors[cell].append((nx, ny))
    print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|115880|192|PyPy3|1685
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys
def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        a = [['*']*(w+4), ['*']+['.']*(w+2)+['*']]
        for _ in range(h):
            a.append(['*', '.'])
            for c in input().rstrip():
                a[-1].append(c)
            a[-1] += ['.', '*']
        a += [['*']+['.']*(w+2)+['*'], ['*']*(w+4)]
        keys = [False]*26
        ord_a = ord('a')
        ord_A = ord('A')
        tmp = input().rstrip()
        if tmp != '0':
            for c in tmp:
                keys[ord(c)-ord_a] = True
        stack = [(1, 1)]
        directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
        waitings = [[] for _ in range(26)]
        ans = 0
        while stack:
            i, j = stack.pop()
            if a[i][j] == '*':
                continue
            ord_aij = ord(a[i][j])
            if 0 <= (tmp := ord_aij-ord_A) < 26 and not keys[tmp]:
                waitings[tmp].append((i, j))
                continue
            elif 0 <= (tmp := ord_aij-ord_a) < 26 and not keys[tmp]:
                keys[tmp] = True
                stack += waitings[tmp]
            elif a[i][j] == '$':
                ans += 1
            a[i][j] = '*'
            for di, dj in directions:
                stack.append((i+di, j+dj))
        print(ans)
main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
peter5264|32140|104|Python3|1354
#### **📝해설**

```python
from collections import deque

T = int(input())

for testcase in range(T):
    h, w = map(int, input().split())
    table = [list(input()) for _ in range(h)]

    # 바깥 아무데서나 들어올 수 있기 때문에, 모든 끝부분에 빈공간 추가
    h += 2
    w += 2

    new_table = [['.'] * w for _ in range(h)]
    for i in range(1, h-1):
        for j in range(1, w-1):
            new_table[i][j] = table[i-1][j-1]
    
    # 현재 갖고 있는 키를 set로 저장
    keys = set(input())
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 방문 여부
    visited = [[False] * w for _ in range(h)]

    # 왼쪽위부터 시작
    q = deque([(0, 0)])
    visited[0][0] = True

    # 현재 들어가고있지 못하는 문을 딕셔너리로 저장
    doors = {chr(c): [] for c in range(ord('A'), ord('Z') + 1)}

    # 찾을 수 있는 문서의 개수
    count = 0

    # BFS 시작
    while q:
        x, y = q.popleft()

        # 상하좌우를 탐색하면서
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 인덱스를 벗어나지 않고 방문한 적 없다면 방문
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                cell = new_table[nx][ny]

                # 벽이라면 넘어감
                if cell == '*':
                    continue

                visited[nx][ny] = True

                # 빈공간은 바로 방문
                if cell == '.':
                    q.append((nx, ny))
                
                # 문서가 있는 위치라면 문서의 개수를 더하고 방문
                elif cell == '$':
                    q.append((nx, ny))
                    count += 1

                # 열쇠가 있는 위치라면
                elif 'a' <= cell <= 'z':

                    # 아직 열쇠를 갖고있지 않았다면
                    if cell not in keys:

                        # 추가
                        keys.add(cell)
                        door_char = cell.upper()

                        # 현재까지 만났던 해당 문을 모두 큐에 추가
                        while doors[door_char]:
                            q.append((doors[door_char].pop()))
                    
                    q.append((nx, ny))
                
                # 문이 있는 위치라면
                elif 'A' <= cell <= 'Z':

                    # 열쇠가 있다면 바로 방문
                    if cell.lower() in keys:
                        q.append((nx, ny))
                    
                    # 열쇠가 없다면, 열쇠를 얻은 후에 방문하게끔 저장
                    else:
                        doors[cell].append((nx, ny))
    print(count)
```