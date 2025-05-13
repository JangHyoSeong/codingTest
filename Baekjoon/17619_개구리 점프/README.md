# [17619] 개구리 점프

### **난이도**
골드 3
## **📝문제**
통나무 N개가 가로 (수평) 방향으로 연못에 떠 있다. 개구리는 한 통나무 A에서 다른 통나무 B로 정확히 수직 방향으로 점프할 수 있다. 단, 점프할 때 다른 통나무 위를 (끝 점 포함) 지나면 안된다.

예를 들어 <그림 1>에서 1번 통나무에서 2번 통나무로 점선을 따라 개구리가 점프하는 것이 가능하다. 1번 통나무에서 2번 통나무로 점프한 후 다시 3번 통나무로 점프하면 1번 통나무에서 3번 통나무로 이동하는 것이 가능하다. (통나무 위에서 걸어서 움직이는 것은 언제든 가능하다.)

[이미지](https://upload.acmicpc.net/98a76e73-0187-43bb-90f9-435f8055e74f/-/preview/)

<그림 1>

통나무들의 위치를 입력받아 질문으로 주어진 통나무들의 쌍에 대해서 개구리가 한 통나무에서 다른 통나무로 한번 이상의 점프로 이동이 가능한지 판단하는 프로그램을 작성하라.
### **입력**
첫 번째 줄에 통나무 개수 N과 질문의 개수 Q가 주어진다. 다음 N개의 줄에 각 통나무에 x1, x2, y의 세 정수 좌표가 주어진다. 주어진 통나무는 두 점 (x1, y)와 (x2, y)를 잇는 형태이다. (x1 < x2) 모든 좌표는 0이상 109이하이다. 통나무들은 주어진 순서대로 1번부터 번호가 붙어 있다. 서로 다른 두 통나무는 (끝점에서도) 만나지 않는다. 다음 Q개의 줄에 서로 다른 두 통나무의 번호가 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ Q ≤ 100,000)
### **출력**
Q개의 줄을 출력한다. 각 줄에는 주어진 순서대로 질문에 대한 대답이 출력되어야 한다. 질문에 주어진 두 통나무에 대해서 개구리가 한 통나무에서 다른 통나무로 한번 이상의 점프로 이동이 가능한 경우 대답은 1, 그렇지 않은 경우 대답은 0이다.
### **예제입출력**

**예제 입력1**

```
4 2
1 5 2
3 7 4
7 9 1
10 13 4
1 3
1 4
```

**예제 출력1**

```
1
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[max(root_x, root_y)] = min(root_x, root_y)

N, Q = map(int, sys.stdin.readline().split())

logs = [list(map(int, sys.stdin.readline().split())) + [i] for i in range(N)]
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]

logs.sort(key=lambda x: x[0])

parent = list(range(N))
right_end = logs[0][1]

for i in range(N-1):

    right_end = max(right_end, logs[i][1])
    if right_end >= logs[i+1][0]:
        union(logs[i][3], logs[i+1][3])

for i in range(N):
    find(i)

for a, b in queries:
    if find(a - 1) == find(b - 1):
        print(1)
    else:
        print(0)

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|136400|412|PyPy3|801
#### **📝해설**

**알고리즘**
```
1. 유니온 파인드
```

### **다른 풀이**

```python
import sys
input=sys.stdin.readline

n,Q = map(int,input().split())
l = []
for i in range(n):
    x1, x2, y = map(int,input().split())
    l.append((x1, x2, i+1))
l.sort(key = lambda x: (x[0]))
s = 0
e = 0
g = 0
dt = [0] * (n+1)
for i in range(n):
    if e < l[i][0]:
        s = l[i][0]
        e = l[i][1]
        g += 1
    else:
        if e < l[i][1]:
            e = l[i][1]
    dt[l[i][2]] = g
for _ in range(Q):
    q1,q2 = map(int,input().split())
    if dt[q1] == dt[q2]:
        print(1)
    else:
        print(0)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jhlee142|125720|292|PyPy3|525
#### **📝해설**

```python
import sys

# 유니온 파인드 부모 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 분리집합을 합치는 함수
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[max(root_x, root_y)] = min(root_x, root_y)

# 입력받기
N, Q = map(int, sys.stdin.readline().split())

logs = [list(map(int, sys.stdin.readline().split())) + [i] for i in range(N)]
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]

# 시작점 기준으로 정렬
logs.sort(key=lambda x: x[0])

# 각 부모의 인덱스를 저장하는 리스트
parent = list(range(N))

# 현재 점프로 갈 수 있는 통나무들의 집합에서, 가장 오른쪽 끝점
right_end = logs[0][1]

# 통나무와 그 다음 통나무들을 검사(정렬되어있기에 가능)
for i in range(N-1):
    # 오른쪽 끝 점을 갱신
    right_end = max(right_end, logs[i][1])

    # 오른쪽 끝 점이 다음 통나무의 시작점보다 뒤에있다면 이동 가능
    if right_end >= logs[i+1][0]:
        # 하나의 집합으로 합침
        union(logs[i][3], logs[i+1][3])

# 경로 압축
for i in range(N):
    find(i)

# 쿼리를 검사
for a, b in queries:
    if find(a - 1) == find(b - 1):
        print(1)
    else:
        print(0)
```