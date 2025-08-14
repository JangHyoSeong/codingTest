# [2251] 물통

### **난이도**
골드 4
## **📝문제**
각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다. 처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다. 이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데, 이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다. 이 과정에서 손실되는 물은 없다고 가정한다.

이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다. 첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오.
### **입력**
첫째 줄에 세 정수 A, B, C가 주어진다.
### **출력**
첫째 줄에 공백으로 구분하여 답을 출력한다. 각 용량은 오름차순으로 정렬한다.
### **예제입출력**

**예제 입력1**

```
8 9 10
```

**예제 출력1**

```
1 2 8 9 10
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

A, B, C = map(int, input().split())
q = deque([(0, 0)])

visited = [[False] * (B + 1) for _ in range(A + 1)]
visited[0][0] = True
result = set()

def pour(x, y, cap_y):
    amount = min(x, cap_y - y)
    return x - amount, y + amount

while q:
    a, b= q.popleft()
    c = C - a - b

    if a == 0:
        result.add(c)
    
    # A → B
    na, nb = pour(a, b, B)
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # A → C
    na, nc = pour(a, c, C)
    if not visited[na][b]:
        visited[na][b] = True
        q.append((na, b))

    # B → A
    nb, na = pour(b, a, A)
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # B → C
    nb, nc = pour(b, c, C)
    if not visited[a][nb]:
        visited[a][nb] = True
        q.append((a, nb))

    # C → A
    nc, na = pour(c, a, A)
    if not visited[na][b]:
        visited[na][b] = True
        q.append((na, b))

    # C → B
    nc, nb = pour(c, b, B)
    if not visited[a][nb]:
        visited[a][nb] = True
        q.append((a, nb))

print(*sorted(result))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34992|56|Python3|1136
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

def solution():
    A, B, C = map(int, input().split())
    visited = [[False]*(B+1) for _ in range(A+1)]
    stack = [(0, 0)]
    res = []
    while stack:
        a, b = stack.pop()
        if visited[a][b]:
            continue
        visited[a][b] = True
        c = C-a-b
        if a == 0:
            res.append(c)
        d = min(a, B-b)
        stack.append((a-d, b+d))
        d = min(a, C-c)
        stack.append((a-d, b))
        d = min(b, A-a)
        stack.append((a+d, b-d))
        d = min(b, C-c)
        stack.append((a, b-d))
        d = min(c, A-a)
        stack.append((a+d, b))
        d = min(c, B-b)
        stack.append((a, b+d))
    print(*sorted(res))

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|31120|32|Python3|732
#### **📝해설**

```python
from collections import deque

# 입력받기
A, B, C = map(int, input().split())

# BFS를 통해 현재 물통에 들어있는 물 양을 구함(a, b) -> 물통 C의 양은 a, b를 통해 알아낼 수 있음
q = deque([(0, 0)])

# 각 물통의 물 양 방문 여부
# C의 경우 A, B를 통해 알아낼 수 있으니 생략
visited = [[False] * (B + 1) for _ in range(A + 1)]
visited[0][0] = True
result = set()

# x에서 y로 물을 붓는 함수
def pour(x, y, cap_y):
    amount = min(x, cap_y - y)
    return x - amount, y + amount

# BFS 시작
while q:

    # a, b, c를 구함
    a, b= q.popleft()
    c = C - a - b

    # a == 0인 경우, 그 때 C 물통의 물 양을 결과로 추가
    if a == 0:
        result.add(c)
    
    # 물붓기
    # A → B
    na, nb = pour(a, b, B)

    # 아직 만든 적 없는 케이스라면 방문 처리
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # A → C
    na, nc = pour(a, c, C)
    if not visited[na][b]:
        visited[na][b] = True
        q.append((na, b))

    # B → A
    nb, na = pour(b, a, A)
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # B → C
    nb, nc = pour(b, c, C)
    if not visited[a][nb]:
        visited[a][nb] = True
        q.append((a, nb))

    # C → A
    nc, na = pour(c, a, A)
    if not visited[na][b]:
        visited[na][b] = True
        q.append((na, b))

    # C → B
    nc, nb = pour(c, b, B)
    if not visited[a][nb]:
        visited[a][nb] = True
        q.append((a, nb))

print(*sorted(result))
```