# [15558] 점프 게임

### **난이도**
골드 5
## **📝문제**
상근이는 오른쪽 그림과 같은 지도에서 진행하는 게임을 만들었다.

지도는 총 2개의 줄로 나누어져 있으며, 각 줄은 N개의 칸으로 나누어져 있다. 칸은 위험한 칸과 안전한 칸으로 나누어져 있고, 안전한 칸은 유저가 이동할 수 있는 칸, 위험한 칸은 이동할 수 없는 칸이다.

가장 처음에 유저는 왼쪽 줄의 1번 칸 위에 서 있으며, 매 초마다 아래 세 가지 행동중 하나를 해야 한다.

- 한 칸 앞으로 이동한다. 예를 들어, 현재 있는 칸이 i번 칸이면, i+1번 칸으로 이동한다.
- 한 칸 뒤로 이동한다. 예를 들어, 현재 있는 칸이 i번 칸이면, i-1번 칸으로 이동한다.
- 반대편 줄로 점프한다. 이때, 원래 있던 칸보다 k칸 앞의 칸으로 이동해야 한다. 예를 들어, 현재 있는 칸이 왼쪽 줄의 i번 칸이면, 오른쪽 줄의 i+k번 칸으로 이동해야 한다.  
N번 칸보다 더 큰 칸으로 이동하는 경우에는 게임을 클리어한 것이다.

게임을 재밌게 하기 위해서, 상근이는 1초에 한 칸씩 각 줄의 첫 칸이 사라지는 기능을 만들었다. 즉, 게임을 시작한지 1초가 지나면 1번 칸이 사라지고, 2초가 지나면 2번 칸이 사라진다. 편의상 유저가 먼저 움직이고, 칸이 사라진다고 가정한다. 즉, 이번에 없어질 칸이 3번 칸인데, 상근이가 3번 칸에 있다면, 3번 칸에서 다른 칸으로 이동하고 나서 3번 칸이 없어지는 것이다.

각 칸의 정보가 주어졌을 때, 게임을 클리어 할 수 있는지, 없는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N과 k가 주어진다. (1 ≤ N, k ≤ 100,000)

둘째 줄에는 왼쪽 줄의 정보가 주어진다. i번째 문자가 0인 경우에는 위험한 칸이고, 1인 경우에는 안전한 칸이다. 셋째 줄에는 오른쪽 줄의 정보가 주어지고, 각 문자의 의미는 왼쪽 줄의 의미와 동일하다.

왼쪽 줄의 1번 칸은 항상 안전한 칸이다.
### **출력**
게임을 클리어할 수 있으면 1을, 없으면 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
7 3
1110110
1011001
```

**예제 출력1**

```
1
```

**예제 입력2**

```
6 2
110101
011001
```

**예제 출력2**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

N, k = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(2)]

visited = [[False] * N for _ in range(2)]
visited[0][0] = True
q = deque([(0, 0, 0)])

while q:
    line, idx, time = q.popleft()

    for dx, dy in [(line, idx + 1), (line, idx - 1), (1 - line, idx + k)]:
        if dy >= N:
            print(1)
            exit()
        
        if dy <= time:
            continue

        if arr[dx][dy] == 0 or visited[dx][dy]:
            continue

        visited[dx][dy] = True
        q.append((dx, dy, time + 1))

print(0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|120784|140|PyPy3|637
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
import sys
from collections import deque

N, k = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(2)]

# 방문 여부를 저장할 리스트
visited = [[False] * N for _ in range(2)]
visited[0][0] = True

# BFS를 위한 queue 선언
q = deque([(0, 0, 0)])

# BFS 시작
while q:
    line, idx, time = q.popleft()

    # 다음번 이동으로 가능한 경우를 탐색
    for dx, dy in [(line, idx + 1), (line, idx - 1), (1 - line, idx + k)]:

        # 만약 N을 넘긴다면 종료
        if dy >= N:
            print(1)
            exit()
        
        # 이미 시간이 지나 밟을 수 없다면 고려하지 않음
        if dy <= time:
            continue
        
        # 이미 방문한 위치거나, 안전하지 않은 곳이라면 고려하지 않음
        if arr[dx][dy] == 0 or visited[dx][dy]:
            continue
        
        # 나머지 모든 경우는 방문처리
        visited[dx][dy] = True
        q.append((dx, dy, time + 1))

# N 너머까지 도달하지 못했다면 0을 출력
print(0)
```