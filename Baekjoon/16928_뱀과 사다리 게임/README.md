# [16928] 뱀과 사다리 게임

### **난이도**
골드 5
## **📝문제**
뱀과 사다리 게임을 즐겨 하는 큐브러버는 어느 날 궁금한 점이 생겼다.

주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면, 최소 몇 번만에 도착점에 도착할 수 있을까?

게임은 정육면체 주사위를 사용하며, 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다. 게임은 크기가 10×10이고, 총 100개의 칸으로 나누어져 있는 보드판에서 진행된다. 보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다.

플레이어는 주사위를 굴려 나온 수만큼 이동해야 한다. 예를 들어, 플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, i+4번 칸으로 이동해야 한다. 만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다. 도착한 칸이 사다리면, 사다리를 타고 위로 올라간다. 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다. 즉, 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고, 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.
### **입력**
첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다. x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다. u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다. 항상 100번 칸에 도착할 수 있는 입력만 주어진다.
### **출력**
100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력한다.
### **예제입출력**

**예제 입력1**

```
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
```

**예제 출력1**

```
3
```

**예제 입력2**

```
4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
```

**예제 출력2**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())

ladders = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladders[a] = b

snakes = {}
for _ in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

visited = [False] * 101
q = deque([[1, 0]])

visited[1] = True

while q:
    now, count = q.popleft()

    if now == 100:
        print(count)
        break

    for move in range(1, 7):
        next = now + move
        if next <= 100 and not visited[next]:
            visited[next] = True
            if ladders.get(next) is not None:
                visited[ladders[next]] = True
                q.append([ladders[next], count+1])
            
            elif snakes.get(next) is not None:
                visited[snakes[next]] = True
                q.append([snakes[next], count+1])
            
            else:
                q.append([next, count+1])

```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34220|56|Python3|904
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
a=[*range(101)]
for i in[*open(0)][1:]:j,k=map(int,i.split());a[j]=k
q=[(1,0)];v=[1]*101
while q:
 u,h=q.pop(0)
 for d in range(6):
  n=a[u]+d+1
  if n>99:exit(print(h+1))
  elif v[n]:v[n]=0;q+=[(n,h+1)]
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
joonion|30616|36|Python|203
#### **📝해설**

```python
from collections import deque

N, M = map(int, input().split())

# 사다리 정보를 딕셔너리로 입력
ladders = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladders[a] = b

# 뱀 정보를 딕셔너리로 입력
snakes = {}
for _ in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

# 방문처리 여부
visited = [False] * 101
q = deque([[1, 0]])

# 시작위치 방문처리
visited[1] = True

# BFS
while q:
    now, count = q.popleft()

    # 도착지에 도착하면 종료
    if now == 100:
        print(count)
        break
    
    # 주사위를 굴려 1~6칸 이동
    for move in range(1, 7):

        # 다음 이동할 칸의 위치
        next = now + move

        # 만약 100을 벗어나지 않고, 방문하지 않았다면
        if next <= 100 and not visited[next]:

            # 방문 처리
            visited[next] = True

            # 만약 이 위치에 사다리가 있다면
            if ladders.get(next) is not None:

              # 사다리 도착지점도 방문처리, q에 삽입
                visited[ladders[next]] = True
                q.append([ladders[next], count+1])
            
            # 뱀이 있는 경우도 동일
            elif snakes.get(next) is not None:
                visited[snakes[next]] = True
                q.append([snakes[next], count+1])
            
            # 뱀도, 사다리도 없다면 그 위치를 큐에 삽입
            else:
                q.append([next, count+1])
```