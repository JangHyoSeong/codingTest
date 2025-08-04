# [2253] 점프

### **난이도**
골드 4
## **📝문제**
N(2 ≤ N ≤ 10,000)개의 돌들이 같은 간격으로 놓여 있다. 편의상 순서대로 1, 2, …, N번 돌이라고 부르자. 당신은 현재 1번 돌 위에 있는데, 이 돌들 사이에서 점프를 하면서 N번째 돌로 이동을 하려 한다. 이때 다음 조건들이 만족되어야 한다.

1. 이동은 앞으로만 할 수 있다. 즉, 돌 번호가 증가하는 순서대로만 할 수 있다.
2. 제일 처음에 점프를 할 때에는 한 칸밖에 점프하지 못한다. 즉, 1번 돌에서 2번 돌이 있는 곳으로 점프할 수 있다. 그 다음부터는 가속/감속 점프를 할 수 있는데, 이전에 x칸 점프를 했다면, 다음번에는 속도를 줄여 x-1칸 점프하거나, x칸 점프하거나, 속도를 붙여 x+1칸 점프를 할 수 있다. 물론 점프를 할 때에는 한 칸 이상씩 해야 한다.
3. 각 돌들은 각기 그 크기가 다르고, 그 중 몇 개의 돌은 크기가 너무 작기 때문에 당신은 그러한 돌에는 올라갈 수 없다.  
위와 같은 조건들을 만족하면서 1번 돌에서 N번 돌까지 점프를 해 갈 때, 필요한 최소의 점프 횟수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 두 정수 N, M(0 ≤ M ≤ N-2)이 주어진다. M은 크기가 맞지 않는, 즉 크기가 작은 돌의 개수이다. 다음 M개의 줄에는 크기가 작은 돌들의 번호가 주어진다. 1번 돌과 N번 돌은 충분히 크기가 크다고 가정한다.
### **출력**
첫째 줄에 필요한 최소의 점프 횟수를 출력한다. 만약 N번 돌까지 점프해갈 수 없는 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
19 3
11
6
16
```

**예제 출력1**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
small_stones = set()
for _ in range(M):
    stone = int(sys.stdin.readline().rstrip())
    small_stones.add(stone)

if 2 in small_stones:
    print(-1)
    exit()

dp = [[False] * (142) for _ in range(N+1)]
dp[2][1] = True

q = deque([(2, 1, 1)])

result = -1
while q:
    pos, speed, count = q.popleft()

    if pos == N:
        result = count
        break

    for next_speed in [speed-1, speed, speed+1]:
        if next_speed < 1:
            continue

        next_pos = pos + next_speed
        if next_pos > N or next_pos in small_stones:
            continue

        if not dp[next_pos][next_speed]:
            dp[next_pos][next_speed] = True
            q.append((next_pos, next_speed, count + 1))

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|45852|988|Python3|822
#### **📝해설**

**알고리즘**
```
1. dp
```

### **다른 풀이**

```python
from sys import stdin

N, stone_n = map(int, stdin.readline().split())

stone = set()
for _ in range(stone_n):
    stone.add(int(stdin.readline().rstrip()))

dp  = [[10001]* (int((2*N)**0.5)+2)  for _ in range(N+1)]

dp[1][0] = 0
for i in range(2, N+1):
    if i in stone:
        continue
    for v in range(1,int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1]) +1


ans = min(dp[N])
if ans == 10001:
    print(-1)
else:
    print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
popgun|122900|144|PyPy3|465
#### **📝해설**

```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
small_stones = set()

# 갈 수 없는 돌을 set로 저장
for _ in range(M):
    stone = int(sys.stdin.readline().rstrip())
    small_stones.add(stone)

# 2가 갈 수 없는 돌이라면 무조건 -1
if 2 in small_stones:
    print(-1)
    exit()

# DP배열 dp[pos][speed] : pos위치에서 speed만큼 점프력이 있을 때 도달 할 수 있는지 여부
dp = [[False] * (142) for _ in range(N+1)]

# 시작위치
dp[2][1] = True

# BFS로 최소 횟수 찾기 (위치, 점프력, 이동 횟수)
q = deque([(2, 1, 1)])

result = -1
while q:
    pos, speed, count = q.popleft()

    # N에 도달했다면, 그때의 이동 횟수가 최소값
    if pos == N:
        result = count
        break

    # 다음 지역 탐색
    for next_speed in [speed-1, speed, speed+1]:

        # 속도가 0이면 고려하지 않음
        if next_speed < 1:
            continue
        
        # 다음 위치
        next_pos = pos + next_speed

        # 인덱스를 넘거나, 갈 수 없는 돌은 건너뜀
        if next_pos > N or next_pos in small_stones:
            continue
        
        # 아직 방문한 적 없는 케이스라면
        if not dp[next_pos][next_speed]:

            # 방문처리
            dp[next_pos][next_speed] = True
            q.append((next_pos, next_speed, count + 1))

print(result)
```