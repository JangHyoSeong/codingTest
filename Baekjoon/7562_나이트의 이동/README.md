# [7562] 나이트의 이동

### **난이도**
실버 1
## **📝문제**
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
### **입력**
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
### **출력**
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
### **예제입출력**

**예제 입력1**

```
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
```

**예제 출력1**

```
5
28
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

T = int(input())

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for testcase in range(T):
    N = int(input())
    start= list(map(int, input().split()))
    target = list(map(int, input().split()))

    q = deque([start])
    visited = [[-1] * N for _ in range(N)]
    visited[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()
        if [x, y] == target:
            break
        
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    
    print(visited[target[0]][target[1]])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34968|3016|Python3|741
#### **📝해설**

**알고리즘**
```
1.
```

### **다른 풀이**

```python
# 충분히 가까워질 때까지 greedy한 move
# 충분히 가까운 곳은 하드코딩


tc = int(input())
needed_moves = (
    (0, 3, 2, 3, 2),
    (3, 2, 1, 2, 3),
    (2, 1, 4, 3, 2),
    (3, 2, 3, 2, 3),
    (2, 3, 2, 3, 4),
)
for _ in range(tc):
    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    x, y = abs(a - c), abs(b - d)
    if x > y:  # x가 더 작게, y가 더 크게 맞춰줌 (개념상 x가 세로축, y가 가로축 좌표)
        x, y = y, x

    # 예외처리 파트, 구석에 몰려 있거나 판이 작으면 문제가 생길 수 있음
    oa, ob = l - a - 1, l - b - 1
    oc, od = l - c - 1, l - d - 1
    ab_in_corner = (not a or not oa) and (not b or not ob)
    cd_in_corner = (not c or not oc) and (not d or not od)
    if ab_in_corner:
        if cd_in_corner and x + y == 3:  # 4x4에서 둘 다 구석이고 가로나 세로로 3만큼만 떨어져 있을 때
            print(5)
            continue
        elif x == 1 and y == 1:  # 한 개가 구석에 있고 한 개는 거기서 가로1,세로1만큼 떨어져 있을 때
            print(4)
            continue
    elif cd_in_corner and x == 1 and y == 1:  # 위와 동일
        print(4)
        continue

    ans = 0

    # 중요 : greedy move의 근거는 needed_move에 진입하기 직전의 상태에 따른 횟수를 직접 카운트하여 경우의 수를 따져야 함
    # x,y의 대소관계를 유지한 채로 한 번의 move 단위로 while문으로 수행할 수도 있다.
    # 하지만 2번의 move를 묶어서 세 종류로 나누고, 논리적인 순서로 몇 번씩 수행할 지 알 수 있으므로 이렇게 하였다.

    if y > 7:  # 가로 4 세로 2만큼 greedy move 최대한 수행
        # x,y의 대소관계가 깨지지 않고, x가 0보다 작아지지 않고, y가 4보다 작아지지 않는 최대한의 move
        move = min(y // 4 - 1, x // 2, (y - x) // 2)
        ans += move * 2
        y -= move * 4
        x -= move * 2

    if x > 5:  # 위의 move 조건 중 x,y의 대소관계 때문에 x와 y가 비슷해진 채로 멈춘 경우
        # 두 번 이동으로 가로3 세로3만큼 이동하는 greedy move 수행
        diagonal_move = x // 3 - 1
        # 5,5에서 2,2로 들어가면 망하므로 한 번 덜 가야함
        # 6,6에서 3,3, 6,7에서 3,4, 7,7에서 4,4로 들어가는 것은 정당한 move이므로 x가 6 이상일 때는 가도 됨
        ans += diagonal_move * 2
        x -= diagonal_move * 3
        y -= diagonal_move * 3

    if y > 7:  # x는 최대 5인 상태
        # 두 번 이동으로 가로로만 4 이동하는 move 수행
        # 그 외에는 두 번 이동으로 가로4만큼 이동하는 greedy move 수행
        y_move = y // 4 - 1
        ans += y_move * 2
        y -= y_move * 4

    while y > 4:  # 아직 x,y가 5,5나 4,6이나 4,7 등의 상태가 가능
        # 경우의 수를 따져 봤을 때, 가로2칸 세로1칸씩 직선 진입하면 문제없음
        x = abs(x - 1)
        y -= 2
        ans += 1

    ans += needed_moves[x][y]
    print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
onionfarmer|31120|48|Python3|3133
#### **📝해설**

```python
from collections import deque

T = int(input())

# 나이트의 이동을 리스트로 표현
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for testcase in range(T):
    N = int(input())
    start= list(map(int, input().split()))
    target = list(map(int, input().split()))

    # BFS를 위한 큐
    q = deque([start])

    # 방문여부와 그 때의 이동횟수를 저장
    visited = [[-1] * N for _ in range(N)]
    visited[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()
        if [x, y] == target:
            break
        
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    
    print(visited[target[0]][target[1]])
```