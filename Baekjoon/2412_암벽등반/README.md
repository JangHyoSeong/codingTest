# [2412] 암벽등반

### **난이도**
골드 4
## **📝문제**
어떤 암벽에 n(1 ≤ n ≤ 50,000)개의 홈이 파져 있다. 각각의 홈의 좌표는 (x, y)와 같이 표현되는데, |a - x| ≤ 2이고 |b - y| ≤ 2이면 (x, y)에서 (a, b)로 이동할 수 있다. 이와 같이 홈들을 이용하여 이동하면서 y = T(1 ≤ T ≤ 200,000)일 때까지, 즉 암벽의 정상까지 오르려고 한다.

현재 당신이 있는 위치는 (0, 0)이다. 이 위치에서 시작하여 이동 회수를 최소로 하면서 정상에 오르려고 한다. 정상에 오를 때의 x좌표는 아무 것이나 되어도 상관이 없다.
### **입력**
첫째 줄에 n, T가 주어진다. 다음 n개의 줄에는 각 점의 x, y좌표가 주어진다. 두 좌표는 모두 0이상이며, x좌표는 1,000,000이하, y좌표는 T이하이다. 입력에 현재 위치인 (0, 0)은 주어지지 않는다.
### **출력**
첫째 줄에 최소 이동 회수를 출력한다. 만약, 정상에 오를 수 없으면 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
1 2
6 3
4 1
3 2
0 2
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

n, T = map(int, sys.stdin.readline().rstrip().split())
nodes = {}
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    nodes[(x, y)] = -1

nodes[(0, 0)] = 0

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    if y == T:
        break

    for dx in range(-2, 3, 1):
        for dy in range(-2, 3, 1):
            nx, ny = x + dx, y + dy

            if nodes.get((nx, ny)) is not None:
                if nodes[(nx, ny)] == -1:
                    q.append((nx, ny))
                    nodes[(nx, ny)] = nodes[(x, y)] + 1

else:
    print(-1)
    exit()

print(nodes[(x, y)])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|119472|256|PyPy3|663
#### **📝해설**

**알고리즘**
```
1. BFS
2. 해쉬
```

### **다른 풀이**

```python
import itertools
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, T = map(int, input().split())
homes = set()
for _ in range(n):
    a, b = map(int, input().split())
    homes.add((a, b))
combs = list(itertools.product([-2, -1, 0, 1, 2], repeat=2))


def bfs():

    q = deque([(0, 0, 0)])

    while q:
        x, y, cnt = q.popleft()

        if y == T:
            return cnt

        for dx, dy in combs:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in homes: continue

            homes.remove((nx, ny))
            q.append((nx, ny, cnt + 1))

    return -1


print(bfs())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
wlghsp1|119540|196|PyPy3|641
#### **📝해설**

```python
import sys
from collections import deque

# 입력받기
n, T = map(int, sys.stdin.readline().rstrip().split())

# 딕셔너리로 노드들을 저장
nodes = {}

# 노드 위치를 key, 방문 시의 이동 횟수를 value로 저장
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    nodes[(x, y)] = -1

# 시작 지점 초기화
nodes[(0, 0)] = 0

# BFS 탐색
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    # T에 도달했다면 BFS 종료
    if y == T:
        break

    # 현재 방문할 수 있는 위치들을 확인
    for dx in range(-2, 3, 1):
        for dy in range(-2, 3, 1):
            nx, ny = x + dx, y + dy

            # 해당 위치에 노드가 있다면 방문
            if nodes.get((nx, ny)) is not None:

                # 한번도 방문하지 않은 노드만 방문
                if nodes[(nx, ny)] == -1:
                    q.append((nx, ny))

                    # 이동 횟수 저장
                    nodes[(nx, ny)] = nodes[(x, y)] + 1

# break가 없었다면, T에 도달하지 못했음
else:
    print(-1)
    exit()

# 마지막으로 방문한 위치 이동 횟수 출력
print(nodes[(x, y)])
```